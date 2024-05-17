FROM ghcr.io/paia-playful-ai-arena/mlgame:10.4.5.3

ADD . /game
WORKDIR /game
RUN pip install -r requirements.txt
CMD ["bash"]
