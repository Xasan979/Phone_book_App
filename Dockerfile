FROM python:3.9

WORKDIR /app

COPY phonebook.py .
COPY data.json .

# RUN pip install ..... # если нужно установить зависимости

CMD ["python", "phonebook.py"]