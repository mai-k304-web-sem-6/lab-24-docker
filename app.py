from flask import Flask, jsonify
import mysql.connector as connector

app = Flask(__name__) # Создание нового экземпляр класса Flask, передав текущее имя модуля в качестве аргумента
try: # Подключение к базе данных
    connection = connector.connect(user="root", password="12345", host="172.23.0.2", database="test", port=32000)
except connector.Error as e: # Обработка исключения
    print("Ошибка: Не удалось подключиться к базе данных")
    print(e) # Вывод ошибки в log сервера

@app.get('/getAll') # Функция получения всех пользователей
def get_all():
    cursor.execute("SELECT * from users") # SQL запрос
    data = cursor.fetchone() # Получение данных из запроса
    return jsonify(data) # Отправка данных

@app.get('/getById/<int:user_id>') # Функция получения пользователя по id
def get_by_id(user_id):
    cursor.execute("SELECT * from users WHERE id=" + str(user_id)) # SQL запрос
    data = cursor.fetchone() # Получение данных из запроса
    return jsonify(data) # Отправка данных

if __name__ == "__main__":
    cursor = connection.cursor() # Создания объекта подключения
    # Запуск сервера разработки Flask со следующими настройками:
    # - debug=True:     включает режим отладки
    # - host='0.0.0.0': прослушивание на всех доступных сетевых интерфейсах (не только на локальном хосте)
    # - port=5000:      прослушивание на порту 5000
    app.run(debug=True, host='0.0.0.0', port=5000)

