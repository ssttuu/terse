FROM python:3.5

RUN mkdir -p /acceptance
ADD ./ /acceptance
WORKDIR /acceptance

RUN pip install -r requirements.txt

CMD pytest
