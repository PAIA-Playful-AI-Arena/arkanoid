export tag=latest
export game="pingpong"

docker build \
-t ${game}:${tag} \
-f ./Dockerfile .
