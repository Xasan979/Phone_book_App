import pymysql
import json
import time

def wait_for_mysql(host, user, password, max_attempts=60):
    attempts = 0
    while attempts < max_attempts:
        try:
            connection = pymysql.connect(
                host=host,
                user=user,
                password=password,
                database='phonebook_db'
            )
            connection.close()
            print("MySQL is ready!")
            return True
        except pymysql.MySQLError as e:
            print(f"MySQL connection attempt {attempts} failed: {e}")
            attempts += 1
            time.sleep(5)  # Подождите 5 секунд перед повторной попыткой
    print("Unable to connect to MySQL after maximum attempts.")
    return False

def import_data():
    with open('data.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Подключение к базе данных
    connection = pymysql.connect(
        host='mysql',
        user='phonebook_user',
        password='12345678',  # Пароль, указанный в docker-compose.yml
        database='phonebook_db'
    )

    cursor = connection.cursor()

    # Создание таблицы, если она ещё не существует
    create_table_query = """
    CREATE TABLE IF NOT EXISTS phonebook (
        id INT AUTO_INCREMENT PRIMARY KEY,
        фамилия VARCHAR(255),
        имя VARCHAR(255),
        отчество VARCHAR(255),
        организация VARCHAR(255),
        телефон_рабочий VARCHAR(255),
        телефон_личный VARCHAR(255)
    )
    """
    cursor.execute(create_table_query)

    # Вставка данных из data.json в базу данных
    for entry in data['Guide'].values():
        insert_query = """
        INSERT INTO phonebook (фамилия, имя, отчество, организация, телефон_рабочий, телефон_личный)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        cursor.execute(insert_query, (
            entry['фамилия'],
            entry['имя'],
            entry['отчество'],
            entry['организация'],
            entry['телефон рабочий'],
            entry['телефон личный']
        ))

    connection.commit()
    connection.close()
    print("Data imported successfully!")

if __name__ == "__main__":
    mysql_host = 'mysql'  # Имя хоста MySQL контейнера
    mysql_user = 'phonebook_user'
    mysql_password = '12345678'  # Пароль, указанный в docker-compose.yml

    if wait_for_mysql(mysql_host, mysql_user, mysql_password):
        import_data()
