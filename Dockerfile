FROM python:3-alpine

MAINTAINER Chad Bailey <chadbailey.me>

WORKDIR /helloworld
COPY ./src /helloworld

RUN apk add --no-cache gcc musl-dev libev-dev
RUN pip install -r requirements.txt

EXPOSE 80
CMD ["python", "helloworld.py"]
