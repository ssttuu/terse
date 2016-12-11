FROM python:3.5

RUN mkdir -p /opt/terse
ADD ./ /opt/terse
WORKDIR /opt/terse

EXPOSE 8888

RUN pip install -r requirements.txt

CMD python app/main.py
