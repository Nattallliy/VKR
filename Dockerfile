FROM ubuntu:latest
LABEL authors="MNC"

ENTRYPOINT ["top", "-b"]

