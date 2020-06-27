FROM python:3

LABEL maintainer="Ricardo Martins <ricardo.ifsc@gmail.com>"
LABEL version="1.0"

ADD my_script.py /

RUN pip install pystrich

CMD [ "python", "./my_script.py" ]
