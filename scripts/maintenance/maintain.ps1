Write-Host '🛠 Running maintenance cycle'

docker ps | Select-String infinityx
docker logs infinityx --tail 50

Write-Host '✔ Maintenance complete'
