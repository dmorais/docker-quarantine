FROM python:3.8 

LABEL maintainer="david@gmail.com"

WORKDIR /home/dmorais/covid-stats/

COPY ./requirements.txt . 

RUN pip install -r requirements.txt 

COPY . . 

CMD [ "python", "get-covid.py" ]