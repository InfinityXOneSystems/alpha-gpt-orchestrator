\ = 'C:\Users\JARVIS\AppData\Local\InfinityXOne\CredentialManager'
\ = 'secrets'

if (Test-Path \) {
  robocopy \ \ /MIR /R:1 /W:1 /NFL /NDL | Out-Null
  Write-Host '🔐 Credentials synced'
} else {
  Write-Host '⚠️ Credential source missing'
}
