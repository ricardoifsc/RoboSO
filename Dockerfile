FROM python:3

LABEL maintainer="Bolivar Lagos and Ricardo Martins <ricardo.ifsc@gmail.com>"
LABEL version="1.0"

ADD teste.py /

RUN pip install httplib2 configparser chatterbot setuptools wheel chatterbot-corpus

CMD [ "python", "./teste.py" ]
