export tag="latest"
export game="arkanoid"

docker build \
-t ${game}:${tag} \
-f ./Dockerfile .
