# Notetube_API
## Социальная сеть для публикации личных дневников
### Описание
REST API для социальной сети Notetube. Авторизация пользователей реализована с помощью библиотеки djoser на JWT-токенах.
### Технологии
Python 3.7, Django 3.2.16, djangorestframework 3.12.4, djoser 2.1.0
### Запуск проекта в dev-режиме
1. Склонируйте проект к себе на компьютер
- Для этого из нужной директории в командной строке выполните команду
```
git clone git@github.com:VanZep/Notetube_API.git
```
2. Перейдите в каталог проекта
```
cd Notetube_API
```
3. Создайте виртуальное окружение
- Linux/macOS
```
python3 -m venv venv
```
- Windows
```
python -m venv venv
```
4. Активируйте виртуальное окружение
- Linux/macOS
```
source venv/bin/activate
```
- Windows
```
source venv/Scripts/activate
```
5. Установите зависимости из файла requirements.txt
```
pip install -r requirements.txt
```
6. Перейдите в директорию с файлом manage.py
```
cd notetube_api
```
7. Выполните миграции
```
python manage.py migrate
```
8. Запустите сервер, выполнив команду
```
python manage.py runserver
```
- В ответ Django сообщит, что сервер запущен и проект доступен по адресу [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- Спецификация API с примерами о том, как должен работать проект доступна по адресу [http://127.0.0.1:8000/redoc/](http://127.0.0.1:8000/redoc/)

### Примеры. Некоторые примеры запросов к API.
```
GET
http://127.0.0.1:8000/api/v1/posts/
```
```
response:
{
    "id": 1,
    "author": "user1",
    "text": "Text1",
    "pub_date": "2023-05-18T05:58:58.749761Z",
    "image": null,
    "group": 1
}
```
```
POST
http://127.0.0.1:8000/api/v1/posts/
{
    "text": "Text6",
    "group": 2
}
```
```
response:
{
    "id": 6,
    "author": "user1",
    "text": "Text6",
    "pub_date": "2023-05-18T09:48:35.978993Z",
    "image": null,
    "group": 2
}
```
```
GET
http://127.0.0.1:8000/api/v1/posts/1/comments/
```
```
response:
{
    "id": 1,
    "author": "user2",
    "text": "Comment1",
    "created": "2023-05-18T06:07:46.807512Z",
    "post": 1
}
```
```
PATCH
http://127.0.0.1:8000/api/v1/posts/1/comments/1/
{
    "text": "Comment1"
}
```
```
response:
{
    "id": 1,
    "author": "user1",
    "text": "Comment1",
    "created": "2023-05-18T06:07:46.807512Z",
    "post": 1
}
```
### Автор
***VanZep***
