export tag=3.0.0b1
docker buildx build --platform linux/amd64,linux/arm64/v8 \
-t paia/arkanoid:${tag} \
-f ./Dockerfile .

#push to ghcr.io
docker buildx build --platform linux/amd64,linux/arm64/v8 \
-t ghcr.io/paia-playful-ai-arena/arkanoid:${tag} \
-f ./Dockerfile . --push