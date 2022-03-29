FROM python:3.8.10

COPY ./requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY ./main.py main.py
COPY ./model.pkl model.pkl

EXPOSE 5000

ENV FLASK_APP=main.py
ENV FLASK_RUN_HOST=0.0.0.0

CMD ["flask", "run"]
