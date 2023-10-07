FROM python:3.10

WORKDIR /app
COPY Requirement.txt /app

RUN pip install -r Requirement.txt

CMD ["python", "app.py", "dev", "all"]
