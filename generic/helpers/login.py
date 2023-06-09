import allure
from apis.dm_api_account.models import LoginCredentials


class Login:  # отвечает за авторизацию
    def __init__(self, facade):  # в параметр facade будет приходить класс Facade
        self.facade = facade

    def set_headers(self, headers):
        self.facade.login_api.client.session.headers.update(headers)  # проставление заголовков в клиент

    def login_user(self, login: str, password: str, remember_me: bool = True):  # авторизация польз-ля
        with allure.step("Авторизация пользователя"):
            response = self.facade.login_api.post_v1_account_login(
                json=LoginCredentials(
                    login=login,
                    password=password,
                    rememberMe=remember_me
                )
            )
        return response

    def get_auth_token(self, login: str, password: str, remember_me: bool = True):  # возвращает авторизационный токен X-Dm-Auth-Token
        with allure.step("Получение авторизационного токена X-Dm-Auth-Token"):
            response = self.login_user(login=login, password=password, remember_me=remember_me)
            token = {'X-Dm-Auth-Token': response.headers['X-Dm-Auth-Token']}  # возвращаем словарь
        return token

    def logout_user(self, **kwargs):
        with allure.step("Логаут пользователя"):
            response = self.facade.login_api.delete_v1_account_login(**kwargs)
        return response

    def logout_user_from_all_devices(self, **kwargs):
        with allure.step("Логаут пользователя на всех устройствах"):
            response = self.facade.login_api.delete_v1_account_login_all(**kwargs)
        return response
