# Yatube
## Социальная сеть для публикации личных дневников
### Описание
API для социальной сети Yatube
### Технологии
Python 3.7
Django 3.2.16
djangorestframework 3.12.4
### Запуск проекта в dev-режиме
- Установите виртуальное окружение
```
python -m venv venv
```
- Активируйте виртуальное окружение
```
source venv/Scripts/activate
```
- Установите зависимости из файла requirements.txt
```
pip install -r requirements.txt
```
- Выполните миграции:
```
python manage.py migrate
```
- В папке с файлом manage.py выполните команду:
```
python manage.py runserver
```
- Для просмотра документации введите в своем брузере адрес:
```

### Примеры. Некоторые примеры запросов к API.
```
http://127.0.0.1:8000/redoc/
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
VanZep
