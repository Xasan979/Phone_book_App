FROM python:3.9

WORKDIR /app

COPY phonebook.py .
COPY data.json .
COPY import_data.py .
COPY requirements.txt .

# Установите зависимости из файла requirements.txt
RUN pip install -r requirements.txt

CMD ["python", "phonebook.py"]

