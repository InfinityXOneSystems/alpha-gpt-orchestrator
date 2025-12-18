Write-Host '?? Pushing memory to GCS'
git pull
gsutil -m rsync -r ./memory-gateway gs://infinityx-memory/memory-gateway
