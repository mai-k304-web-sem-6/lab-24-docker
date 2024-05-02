# Начните с извлечения изображения python
FROM python:3.8-alpine
# Скопируйте файл требований в изображение
COPY ./requirements.txt /app/requirements.txt
# Переключить рабочий каталог
WORKDIR /app
# Установите зависимости и пакеты из файла требований
RUN pip install -r requirements.txt
# Скопируйте все содержимое из локального файла в изображение
COPY . /app
# Сконфигурируйте контейнер для запуска в установленном порядке
ENTRYPOINT ["python"]
# Файл который будет запускаться
CMD ["app.py"]