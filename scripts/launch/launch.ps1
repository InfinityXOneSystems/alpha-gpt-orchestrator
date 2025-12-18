Write-Host '🚀 LAUNCHING INFINITY-X' -ForegroundColor Cyan

docker build -t infinityx/orchestrator:latest .
docker run -d 
  --name infinityx 
  -p 8080:8080 
  --restart unless-stopped 
  infinityx/orchestrator:latest

Write-Host '✅ SYSTEM LIVE' -ForegroundColor Green
