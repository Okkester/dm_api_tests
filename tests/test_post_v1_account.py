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
    login = 'strtest11'  # завели три переменные для регистрации->активации->авторизации
    email = 'strtest11@mail.ru'
    password = 'strtest11'

    db = DmDatabase(user='postgres', password='admin', host='localhost', database='dm3.5')
    db.delete_user_by_login(login=login)
    dataset = db.get_user_by_login(login=login)  # получение юзера по его логину чтобы посмотреть появилась ли запись в БД
    assert len(dataset) == 0  # проверка того что такого юзера нет в БД

    api.mailhog.delete_all_messages()  # удаляем все письма пользователя

    response = api.account.register_new_user(  # прописали обёртку над методом из helpers Account
        login=login,
        email=email,
        password=password
    )
    dataset = db.get_user_by_login(login=login)  # получение юзера по его логину чтобы посмотреть появилась ли запись в БД
    for row in dataset:
        assert row['Login'] == login, f'User {login} not registered'  # проверка того что юзер зарегистрирован
        assert row['Activated'] is False, f'User {login} was activated'  # проверка что юзер не активирован

    # activate  user
    api.account.activate_registered_user(login=login)  # прописали обёртку над методом put_v1_account_token из helpers Account
    time.sleep(2)  # чтобы дождаться проставления признака activated в БД
    dataset = db.get_user_by_login(login=login)  # запрос обновлённой инфы по юзеру
    for row in dataset:
        assert row['Activated'] is True, f'User {login} not activated'  # проверка что юзер активирован

    # Login  user
    api.login.login_user(
        login=login,
        password=password
    )









    # Logout  user - ДЗ - Разлогиниться  при передаче заголовков в метод через **kwargs
    # token = api.login.get_auth_token(login='strtest6',
    #                                  password='strtest6')  # возвращает авторизационный токен X-Dm-Auth-Token
    # api.login_api.delete_v1_account_login(headers=token)

    # # Logout  user - ДЗ - Разлогиниться при помощи установки авторизационных заголовков в клиент
    # token = api.login.get_auth_token(login='strtest4', password='strtest4')    # возвращает авторизационный токен X-Dm-Auth-Token
    # api.login.set_headers(headers=token)
    # api.login.logout_user()
