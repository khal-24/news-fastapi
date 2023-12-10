FROM python:3.10

RUN mkdir /src

WORKDIR src

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . src

WORKDIR src

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]