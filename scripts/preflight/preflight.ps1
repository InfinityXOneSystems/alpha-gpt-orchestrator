Write-Host '🔍 PREFLIGHT CHECK STARTING' -ForegroundColor Cyan

python --version
docker --version

if (!(Test-Path 'system_manifest.yaml')) {
  throw 'Manifest missing'
}

if (!(Test-Path 'control\auto_loop.py')) {
  throw 'AutoLoop missing'
}

Write-Host '✅ PREFLIGHT PASSED' -ForegroundColor Green
