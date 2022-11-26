FROM python:3.9.7

WORKDIR /app
# ENV FLASK_APP=app

# COPY ./flaskapp/requirements.txt ./
COPY ./flaskapp .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install gunicorn
RUN sed -i s/'API_VERSION = 1'/'API_VERSION = 1.2'/g /usr/local/lib/python3.9/site-packages/fitbit/api.py

EXPOSE 5000

# CMD ["uwsgi", "--ini", "app.ini"]
CMD ["gunicorn", "app:app", "--log-level=info", "--bind=0.0.0.0:5000", "--error-logfile=-", "--capture-output"]