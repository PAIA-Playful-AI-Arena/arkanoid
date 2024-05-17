docker run -it --rm --name arkanoid \
-v ./ai/user-1:/game/ai/1P \
-v ./records:/game/records \
-v ./var:/game/var  \
-v /tmp/.X11-unix:/tmp/.X11-unix \
-e DISPLAY=host.docker.internal:0 \
arkanoid:3.0.0 \
sh -c "python -m mlgame -1 -f 30 -r /game/records -i /game/ai/1P/ml_play.py /game"