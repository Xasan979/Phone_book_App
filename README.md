# Phone_book_App
Подробно описанный функционал программы:
  
    https://disk.yandex.ru/i/KfCDSTRPQRurNw

## Запуск файла phonebook.py

Откройте командную строку (или терминал, если вы используете Linux/Mac).
С помощью команды cd, перейдите в директорию, содержащую файл phonebook.py.
Используя интерпретатор Python. Вы можете использовать команду python (или python3 на Linux/Mac) с именем файла:

    python phonebook.py

## Запуск файла через Dockerfile.
С помощью команды cd, перейдите в директорию, содержащую файл phonebook.py
    
    docker build -t phonebook-app .

    docker run -it phonebook-app

## Запуск файла через docker-compose. 
### Импорт данных из JSON файла в базу данных MySQL
С помощью команды cd, перейдите в директорию, содержащую файл phonebook.py

     docker-compose up --build

Теперь можно перейти на http://localhost:8080 , для удобной работы с данными в БД