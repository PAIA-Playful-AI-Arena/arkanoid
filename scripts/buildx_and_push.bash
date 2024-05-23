export tag="latest"
export game="pingpong"
#push to ghcr.io
docker buildx build --platform linux/amd64,linux/arm64 \
-t ghcr.io/paia-playful-ai-arena/${game}:${tag} \
-f ./Dockerfile . --push