FROM python:alpine3.15

WORKDIR .
COPY ./log.py ./log.py

CMD ["python3" , "log.py"]

