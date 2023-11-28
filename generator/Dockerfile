FROM python:3.9-slim-bullseye

WORKDIR /generator

COPY requirements.txt generator/requirements.txt

COPY playlist_generator.py generator/playlist_generator.py

RUN pip install -r generator/requirements.txt

CMD ["python", "generator/playlist_generator.py"]
