param(
    [Parameter(Mandatory=$true)][string]$InputPrefix,
    [Parameter(Mandatory=$true)][ValidateRange(1,9999)][int]$FirstPage,
    [Parameter(Mandatory=$true)][ValidateRange(1,9999)][int]$LastPage,
    [string]$Language = 'zh-Hans-CN'
)
# Run under Windows PowerShell 5.1: local OCR, no network or document upload.
$ErrorActionPreference = 'Stop'
if ($LastPage -lt $FirstPage) { throw 'LastPage must be at least FirstPage' }
Add-Type -AssemblyName System.Runtime.WindowsRuntime
$null = [Windows.Storage.StorageFile, Windows.Storage, ContentType=WindowsRuntime]
$null = [Windows.Storage.Streams.IRandomAccessStream, Windows.Storage.Streams, ContentType=WindowsRuntime]
$null = [Windows.Graphics.Imaging.BitmapDecoder, Windows.Graphics.Imaging, ContentType=WindowsRuntime]
$null = [Windows.Graphics.Imaging.SoftwareBitmap, Windows.Graphics.Imaging, ContentType=WindowsRuntime]
$null = [Windows.Media.Ocr.OcrEngine, Windows.Foundation, ContentType=WindowsRuntime]
$null = [Windows.Media.Ocr.OcrResult, Windows.Foundation, ContentType=WindowsRuntime]
$null = [Windows.Globalization.Language, Windows.Globalization, ContentType=WindowsRuntime]
$awaitMethod = [System.WindowsRuntimeSystemExtensions].GetMethods() | Where-Object {
    $_.Name -eq 'AsTask' -and $_.IsGenericMethod -and $_.GetParameters().Count -eq 1 -and
    $_.GetParameters()[0].ParameterType.Name -eq 'IAsyncOperation`1'
} | Select-Object -First 1
function Await-WinRT($Operation, [Type]$ResultType) {
    $task = $awaitMethod.MakeGenericMethod($ResultType).Invoke($null, @($Operation))
    $task.GetAwaiter().GetResult()
}
$engine = [Windows.Media.Ocr.OcrEngine]::TryCreateFromLanguage(
    [Windows.Globalization.Language]::new($Language))
if ($null -eq $engine) { throw "Local OCR language unavailable: $Language" }
for ($page = $FirstPage; $page -le $LastPage; $page++) {
    $imagePath = (Resolve-Path -LiteralPath ('{0}-{1:000}.png' -f $InputPrefix, $page)).Path
    $jsonPath = [IO.Path]::ChangeExtension($imagePath, '.ocr.json')
    $textPath = [IO.Path]::ChangeExtension($imagePath, '.ocr.txt')
    $imageHash = (Get-FileHash -LiteralPath $imagePath -Algorithm SHA256).Hash.ToLowerInvariant()
    if ((Test-Path -LiteralPath $jsonPath) -and (Test-Path -LiteralPath $textPath)) {
        $cached = Get-Content -LiteralPath $jsonPath -Raw -Encoding UTF8 | ConvertFrom-Json
        if ($cached.image_sha256 -eq $imageHash -and $cached.language -eq $Language) {
            Write-Output "OCR page $page cached"
            continue
        }
    }
    $file = Await-WinRT ([Windows.Storage.StorageFile]::GetFileFromPathAsync($imagePath)) ([Windows.Storage.StorageFile])
    $stream = Await-WinRT ($file.OpenAsync([Windows.Storage.FileAccessMode]::Read)) ([Windows.Storage.Streams.IRandomAccessStream])
    try {
        $decoder = Await-WinRT ([Windows.Graphics.Imaging.BitmapDecoder]::CreateAsync($stream)) ([Windows.Graphics.Imaging.BitmapDecoder])
        $bitmap = Await-WinRT ($decoder.GetSoftwareBitmapAsync()) ([Windows.Graphics.Imaging.SoftwareBitmap])
        try {
            $result = Await-WinRT ($engine.RecognizeAsync($bitmap)) ([Windows.Media.Ocr.OcrResult])
            $lines = @($result.Lines | ForEach-Object {
                @{ text = $_.Text; words = @($_.Words | ForEach-Object {
                    @{ text = $_.Text; x = $_.BoundingRect.X; y = $_.BoundingRect.Y;
                       width = $_.BoundingRect.Width; height = $_.BoundingRect.Height }
                }) }
            })
            $data = @{ engine = 'Windows.Media.Ocr'; language = $Language; pdf_page = $page; image_sha256 = $imageHash;
                width = $bitmap.PixelWidth; height = $bitmap.PixelHeight; lines = $lines }
            $utf8 = [Text.UTF8Encoding]::new($false)
            [IO.File]::WriteAllText($jsonPath, ($data | ConvertTo-Json -Depth 8), $utf8)
            [IO.File]::WriteAllText($textPath, (($lines | ForEach-Object { $_.text }) -join "`n"), $utf8)
            Write-Output "OCR page $page saved ($($lines.Count) lines)"
        } finally { $bitmap.Dispose() }
    } finally { $stream.Dispose() }
}
