export tag=3.0.0b1
docker build -t paia/arkanoid:${tag} -t ghcr.io/paia-playful-ai-arena/arkanoid:${tag} -f ./Dockerfile .
