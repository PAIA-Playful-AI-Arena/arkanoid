FROM paia/mlgame:latest

ADD . /game
WORKDIR /game
RUN pip install -r requirements.txt
CMD ["bash"]
