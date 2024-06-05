FROM paiatech/mlgame:10.4.6a1-slim

ADD . /game
WORKDIR /game
RUN pip install -r requirements.txt --no-cache-dir
CMD ["bash"]
