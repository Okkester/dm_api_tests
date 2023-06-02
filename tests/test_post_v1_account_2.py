import time

from generic.helpers.dm_db import DmDatabase
from services.dm_api_account import Facade
import structlog

structlog.configure(
    processors=[  # набор процессоров форматируют наш код в консоли. Процессоры лежат в либе structlog
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]  # параметры процессора: indent - отступ в джсоне, ensure_ascii=False - для работы с русской кодировкой
)


def test_post_v1_account():
    api = Facade(host='http://localhost:5051')  # инициализация
    # register new user
    login = 'strtest125'  # завели три переменные для регистрации->активации->авторизации
    email = 'strtest125@mail.ru'
    password = 'strtest125'

    db = DmDatabase(user='postgres', password='admin', host='localhost', database='dm3.5')

    response = api.account.register_new_user(  # прописали обёртку над методом из helpers Account
        login=login,
        email=email,
        password=password
    )
    # ДЗ - 1 задание (урок 11)

    db.update_activated_status_user_by_login(login=login)
    dataset = db.get_user_by_login(login=login)
    for row in dataset:
        assert row['Activated'] is True, f'User {login} was not activated'  # проверка того что sql-запрос активировал пользователя

    # ДЗ - 2 задание (урок 11)

    api.account.activate_registered_user(login=login)
    time.sleep(2)  # чтобы дождаться проставления признака activated в БД
    dataset = db.get_user_by_login(login=login)  # запрос обновлённой инфы по юзеру
    for row in dataset:
        assert row['Activated'] is False, f'User {login} already activated'  # проверка что юзер уже активирован
