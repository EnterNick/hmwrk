FROM python:3.13

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt --no-cache-dir

COPY . .

EXPOSE 8000

CMD ["sh", "-c", "sleep 10 && python manage.py runserver 0.0.0.0:8000"]
