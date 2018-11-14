FROM frolvlad/alpine-python3

MAINTAINER Chad Bailey <chadbailey.me>

WORKDIR /helloworld
COPY ./src /helloworld

RUN apk add --no-cache gcc musl-dev libev-dev python3-dev
RUN pip install -r requirements.txt

EXPOSE 80
CMD ["python", "helloworld.py"]
