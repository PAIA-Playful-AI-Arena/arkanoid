export tag=latest
docker build \
-t arkanoid:${tag} \
-f ./Dockerfile .
