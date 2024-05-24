FROM paiatech/mlgame:10.4.5.3

ADD . /game
WORKDIR /game
RUN pip install -r requirements.txt --no-cache-dir
CMD ["bash"]
