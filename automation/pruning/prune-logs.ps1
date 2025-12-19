$cutoff = (Get-Date).AddDays(-14)
Get-ChildItem logs/runtime -Recurse |
Where-Object { $_.LastWriteTime -lt $cutoff } |
Remove-Item -Force
