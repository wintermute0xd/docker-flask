FROM python:3

WORKDIR /usr/flaskapp

COPY ./requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY ./app.py ./

# CMD ["flask", "run", "--host=0.0.0.0"]
CMD ["gunicorn", "-w", "2", "-b", "0.0.0.0", "app:app"]