# Проект YamDb

Проект YaMDb собирает отзывы пользователей на произведения.

Произведению может быть присвоен жанр. Новые жанры может создавать только администратор.

Пользователи могут оставлять текстовые отзывы и комментарии к отзывам,
поставить оценку от 1 до 10.

Из пользовательских оценок формируется рейтинг произведений.

## Функционал API:

Просмотр произведений которые подразделяются по жанрам и категориям.

Возможность добавлять произведения, оставлять отзывы и ставить оценки произведениям.

Каждый отзыв можно прокомментировать.

*Проект разработан командой из двух человек рамках учебного курса Яндекс.Практикум, когорта №49*

## Разработчики:

Алексей Ивлев https://github.com/Theivlev

Сергей Свешников https://github.com/SerejaSpace

## Технологии:

*Python 3.7.9*

*Django 3.2*

*Django REST Framework 3.12.4*

*Djangorestframework-simplejwt 4.8.0*

# Как запустить проект:

## Cоздать и активировать виртуальное окружение:

*WIN: python -m venv venv*

*MAC: python3 -m venv venv*

*WIN: source venv/scripts/activate*

*MAC: source venv/bin/activate*

# Установить зависимости из файла requirements.txt:

*WIN: python -m pip install --upgrade pip*

*MAC: python3 -m pip install --upgrade pip*

*pip install -r requirements.txt*

# Выполнить миграции:

*WIN: python manage.py migrate*

*MAC: python3 manage.py migrate*

# Запустить проект:

*WIN: python manage.py runserver*

*MAC: python3 manage.py runserver*

## Документация:
*Полная документация и примеры запросов доступны по эндпоинту*

http://127.0.0.1:8000/redoc/
