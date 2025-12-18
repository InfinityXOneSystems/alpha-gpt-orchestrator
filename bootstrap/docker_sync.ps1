docker build -t alpha-gpt-orchestrator:latest .
docker stop alpha-gpt-orchestrator 2>
docker rm alpha-gpt-orchestrator 2>
docker run -d --name alpha-gpt-orchestrator -p 8080:8080 alpha-gpt-orchestrator
