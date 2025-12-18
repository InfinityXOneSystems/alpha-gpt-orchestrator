# Cloud Scheduler Job (create in GCP):
#
# Frequency: every 5 minutes
# Target: HTTP
# URL: https://orchestrator-896380409704.us-east1.run.app/heartbeat
# Auth: OIDC using service account
#
# This guarantees 24/7 execution even if Neo is offline.
