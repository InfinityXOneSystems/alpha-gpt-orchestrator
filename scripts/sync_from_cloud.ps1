Write-Host '?? Pulling memory from GCS'
gsutil -m rsync -r gs://infinityx-memory/memory-gateway ./memory-gateway

git add memory-gateway
git commit -m 'sync: cloud ? local memory' -a
git push
