FROM python:3.9-slim-bullseye

WORKDIR /frontend

COPY requirements.txt frontend/requirements.txt

COPY app.py frontend/app.py

RUN pip3 install -r frontend/requirements.txt

EXPOSE 32180

CMD ["python", "/frontend/app.py","--host=0.0.0.0" ,"--host=32180"]
