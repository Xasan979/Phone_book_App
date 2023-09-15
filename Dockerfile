# Используем базовый образ Python версии 3.9
FROM python:3.9

# Устанавливаем рабочий каталог внутри контейнера на /app
WORKDIR /app

# Копируем файлы из текущего контекста сборки в /app внутри контейнера
COPY phonebook.py .
COPY data.json .
COPY import_data.py .
COPY requirements.txt .

# Установка зависимостей из файла requirements.txt
RUN pip install -r requirements.txt

# Команда, выполняемая при запуске контейнера
CMD ["python", "phonebook.py"]

