FROM python:3

LABEL maintainer="Bolivar Lagos and Ricardo Martins <ricardo.ifsc@gmail.com>"
LABEL version="1.0"

ADD programa.py /

RUN pip install httplib2 configparser

CMD [ "python", "./my_script.py" ]
