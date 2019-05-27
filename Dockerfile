FROM ubuntu:18.04

RUN apt update -y
RUN apt install build-essential clang -y

WORKDIR /playground

# docker build -t cosasdepuma/dev:alfredcpp .
# docker run --rm --interactive --tty --volume $PWD:/playground cosasdepuma/dev:alfredcpp