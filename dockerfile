FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt requirements.txt

# Install dependencies
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "train.py"]
