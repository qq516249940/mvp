FROM python:3.8
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE=1

ADD /backend /tancho/
ADD requirements.txt /tancho/
WORKDIR /tancho

RUN pip install -r requirements.txt
