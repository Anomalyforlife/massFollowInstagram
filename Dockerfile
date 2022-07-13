FROM python:3.9

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

USER 1000

CMD [ "python", "./main.py" ]