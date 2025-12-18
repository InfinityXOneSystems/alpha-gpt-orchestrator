## Architecture Overview

- Single orchestrator container
- FastAPI control plane
- Background autonomy loop
- Manifest-governed behavior
- Plugin-driven UI + capability exposure
- Vertex AI for prediction confidence
- Firestore / RAG memory

Startup Flow:
1. Load manifest
2. Initialize subsystems
3. Start AutoLoop
4. Expose API
5. Begin intelligence ingestion
