import time
import pytest
from hamcrest import assert_that, has_entries
from collections import namedtuple
from string import ascii_letters, digits
import random


@pytest.fixture
def prepare_user(dm_api_facade, dm_db):
    user = namedtuple('User',
                      'login, email, password')  # объект namedtuple 'User',в котором указаны хранимые в нём поля
    User = user(login="intest28", email="intest28@mail.ru", password="intest28")
    dm_db.delete_user_by_login(login=User.login)  # удаление юзера из БД
    dataset = dm_db.get_user_by_login(login=User.login)
    assert len(dataset) == 0  # проверка того что такого юзера нет в БД
    dm_api_facade.mailhog.delete_all_messages()  # удаляем все письма пользователя
    return User


def test_post_v1_account(dm_api_facade, dm_db, prepare_user):
    # register new user
    login = prepare_user.login
    email = prepare_user.email
    password = prepare_user.password
    response = dm_api_facade.account.register_new_user(  # прописали обёртку над методом из helpers Account
        login=login,
        email=email,
        password=password
    )
    dataset = dm_db.get_user_by_login(
        login=login)  # получение юзера по его логину чтобы посмотреть появилась ли запись в БД
    for row in dataset:
        assert_that(row, has_entries(
            {
                'Login': login,
                'Activated': False
            }
        ))
    # activate  user
    dm_api_facade.account.activate_registered_user(
        login=login)  # прописали обёртку над методом put_v1_account_token из helpers Account
    time.sleep(2)  # чтобы дождаться проставления признака activated в БД
    dataset = dm_db.get_user_by_login(login=login)  # запрос обновлённой инфы по юзеру
    for row in dataset:
        assert row['Activated'] is True, f'User {login} not activated'  # проверка что юзер активирован

    # Login  user
    dm_api_facade.login.login_user(
        login=login,
        password=password
    )


@pytest.mark.parametrize('login, email, password', [  # пишем какие поля меняем и в кортеже перечисляем тестовые значения
    ('intest29', 'intest29@mail.ru', 'intest29'),
    ('intestttt', 'intesttt@mail.ru', 'intestttt'),
    ('234343429', '34623423429@mail.ru', '2345234529'),
    ('/////////', '//////////@mail.ru', '///////////')
])
def random_string():
    symbols = ascii_letters + digits
    string = ''
    for _ in range(10):
        string += random.choice(symbols)
    return string


@pytest.mark.parametrize('login', [random_string() for _ in range(3)])
@pytest.mark.parametrize('email', [random_string() + '@' + random_string() + '.ru' for _ in range(3)])
@pytest.mark.parametrize('password', [random_string() for _ in range(3)])
def test_post_v1_account_2(dm_api_facade, dm_db, login, email, password):
    dm_db.delete_user_by_login(login=login)
    dm_api_facade.mailhog.delete_all_messages()

    # register new user
    response = dm_api_facade.account.register_new_user(  # прописали обёртку над методом из helpers Account
        login=login,
        email=email,
        password=password
    )
    dataset = dm_db.get_user_by_login(
        login=login)  # получение юзера по его логину чтобы посмотреть появилась ли запись в БД
    for row in dataset:
        assert_that(row, has_entries(
            {
                'Login': login,
                'Activated': False
            }
        ))
    # activate  user
    dm_api_facade.account.activate_registered_user(
        login=login)  # прописали обёртку над методом put_v1_account_token из helpers Account
    time.sleep(2)  # чтобы дождаться проставления признака activated в БД
    dataset = dm_db.get_user_by_login(login=login)  # запрос обновлённой инфы по юзеру
    for row in dataset:
        assert row['Activated'] is True, f'User {login} not activated'  # проверка что юзер активирован

    # Login  user
    dm_api_facade.login.login_user(
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


def random_string_2(begin=1, end=30):
    symbols = ascii_letters + digits
    string = ''
    for _ in range(random.randint(begin, end)):
        string += random.choice(symbols)
    return string


@pytest.mark.parametrize('login, email, password, status_code, login_check', [
    ('14', '14@14.ru', '12334567', 201, ''),  # Валидные данные
    ('13', '13@13.ru', random_string_2(1, 5), 400, {"Password": ["Short"]}),  # Пароль <= 5 символам
    ('2', '13@13.ru', '1234567', 400, {"Login": ["Short"]}),  # Логин менее 2 символов
    ('13', '13@', '1234567', 400, {"Email": ["Invalid"]}),  # Email не содержит доменную часть
    ('13', '13', '1234567', 400, {"Email": ["Invalid"]}),  # Email не содержит символ @
])
def test_create_and_activate_user_with_random_params(
        dm_api_facade,
        dm_db,
        login,
        email,
        password,
        status_code,
        # password_check,
        login_check
        # email_check
):
    dm_db.delete_user_by_login(login=login)
    dm_api_facade.mailhog.delete_all_messages()

    # register new user
    response = dm_api_facade.account.register_new_user_2(  # прописали обёртку над методом из helpers Account
        login=login,
        email=email,
        password=password,
        status_code=status_code
    )
    if status_code == 201:
        dataset = dm_db.get_user_by_login(
            login=login)  # получение юзера по его логину чтобы посмотреть появилась ли запись в БД
        for row in dataset:
            assert_that(row, has_entries(
                {
                    'Login': login,
                    'Activated': False
                }
            ))
        # activate  user
        dm_api_facade.account.activate_registered_user(
            login=login)  # прописали обёртку над методом put_v1_account_token из helpers Account
        time.sleep(2)  # чтобы дождаться проставления признака activated в БД
        dataset = dm_db.get_user_by_login(login=login)  # запрос обновлённой инфы по юзеру
        for row in dataset:
            assert row['Activated'] is True, f'User {login} not activated'  # проверка что юзер активирован

        # Login  user
        dm_api_facade.login.login_user(
            login=login,
            password=password
        )
    else:
        assert_that(response.json()['errors'], has_entries(
            {
                # "Password": ["Short"],
                "Login": ["Short"]
                # "Email": ["Invalid"]
            }
        ))
