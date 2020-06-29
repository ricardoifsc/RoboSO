FROM python:3

LABEL maintainer="Bolivar Lagos and Ricardo Martins <ricardo.ifsc@gmail.com>"
LABEL version="1.0"

ADD teste.py /

COPY config.ini /

RUN pip install pycurl requests configparser

CMD [ "python", "./teste.py" ]
