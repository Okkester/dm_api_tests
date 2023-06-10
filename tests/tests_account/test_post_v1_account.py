import allure
import pytest
from hamcrest import assert_that, has_entries
from collections import namedtuple
from string import ascii_letters, digits
import random
from data.post_v1_account import PostV1AccountData as user_data


def random_string():
    symbols = ascii_letters + digits
    string = ''
    for _ in range(10):
        string += random.choice(symbols)
    return string


def random_string_2(begin=1, end=30):
    symbols = ascii_letters + digits
    string = ''
    for _ in range(random.randint(begin, end)):
        string += random.choice(symbols)
    return string


@allure.suite("Тесты на проверку метода POST{host}/v1/account")
@allure.sub_suite("Позитивные проверки")
class TestsPostV1Account:
    @allure.step("Подготовка тестовго пользователя")
    @pytest.fixture
    def prepare_user(self, dm_api_facade, dm_db):
        user = namedtuple('User',
                          'login, email, password')  # объект namedtuple 'User',в котором указаны хранимые в нём поля
        User = user(login=user_data.login, email=user_data.email, password=user_data.password)
        dm_db.delete_user_by_login(login=User.login)  # удаление юзера из БД
        dataset = dm_db.get_user_by_login(login=User.login)
        assert len(dataset) == 0  # проверка того что такого юзера нет в БД
        dm_api_facade.mailhog.delete_all_messages()  # удаляем все письма пользователя
        return User

    @allure.title("Проверка регистрации и активации пользователя")
    def test_register_and_activate_user(self, dm_api_facade, dm_db, prepare_user, assertions):
        """
        Тест проверяет создание и активацию пользователя в базе данных
        """
        # register new user
        login = prepare_user.login
        email = prepare_user.email
        password = prepare_user.password
        dm_api_facade.account.register_new_user(  # прописали обёртку над методом из helpers Account
            login=login,
            email=email,
            password=password
        )
        assertions.check_user_was_created(login=login)
        # activate  user
        dm_api_facade.account.activate_registered_user(
            login=login)  # прописали обёртку над методом put_v1_account_token из helpers Account
        assertions.check_user_was_activated(login=login)
        # Login  user
        dm_api_facade.login.login_user(
            login=login,
            password=password
        )

    @pytest.mark.parametrize('login', [random_string() for _ in range(3)])
    @pytest.mark.parametrize('email', [random_string() + '@' + random_string() + '.ru' for _ in range(3)])
    @pytest.mark.parametrize('password', [random_string() for _ in range(3)])
    def test_create_and_activated_user_with_random_params(
            self,
            dm_api_facade,
            dm_db,
            login,
            email,
            password,
            assertions
    ):
        dm_db.delete_user_by_login(login=login)
        dm_api_facade.mailhog.delete_all_messages()
        # register new user
        dm_api_facade.account.register_new_user(  # прописали обёртку над методом из helpers Account
            login=login,
            email=email,
            password=password
        )
        assertions.check_user_was_created(login=login)
        # activate  user
        dm_api_facade.account.activate_registered_user(
            login=login)  # прописали обёртку над методом put_v1_account_token из helpers Account
        assertions.check_user_was_activated(login=login)
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

    @pytest.mark.parametrize('login, email, password, status_code, check_error', [
        ('14', '14@14.ru', '12334567', 201, ''),  # Валидные данные
        ('15', '15@15.ru', random_string_2(1, 5), 400, {"Password": ["Short"]}),  # Пароль <= 5 символам
        ('2', '16@16.ru', '1234567', 400, {"Login": ["Short"]}),  # Логин менее 2 символов
        ('17', '17@', '1234567', 400, {"Email": ["Invalid"]}),  # Email не содержит доменную часть
        ('18', '18', '1234567', 400, {"Email": ["Invalid"]}),  # Email не содержит символ @
    ])
    def test_create_and_activate_user_with_random_params(
            self,
            dm_api_facade,
            dm_db,
            login,
            email,
            password,
            status_code,
            check_error,
            assertions
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
        assertions.check_user_was_created(login=login)
        # activate  user
        if status_code == 201:
            dm_api_facade.account.activate_registered_user(
                login=login)  # прописали обёртку над методом put_v1_account_token из helpers Account
            assertions.check_user_was_activated(login=login)
            # Login  user
            dm_api_facade.login.login_user(
                login=login,
                password=password
            )
        else:
            assert_that(response.json()['errors'], has_entries(check_error))
