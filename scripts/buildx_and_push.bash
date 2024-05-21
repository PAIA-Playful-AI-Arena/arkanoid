export tag="latest"
#push to ghcr.io
docker buildx build --platform linux/amd64,linux/arm64 \
-t ghcr.io/paia-playful-ai-arena/arkanoid:${tag} \
-f ./Dockerfile . --push