from apis.dm_api_account.models import Registration
import allure
try:
    from services.dm_api_account import Facade
except ImportError:
    ...


class Account:  # отвечает за регистрацию и активацию юзера
    def __init__(self, facade: Facade): # в параметр facade будет приходить класс Facade
        self.facade = facade

    # ниже функции описывают обёртки над методами
    def set_headers(self, headers):  # установка заголовков в клиент
        self.facade.account_api.client.session.headers.update(headers)

    def register_new_user(self, login: str, email: str, password: str):
        with allure.step("Регистрация нового пользователя"):
            response = self.facade.account_api.post_v1_account(
                json=Registration(  # вынесли Registration не как модель, а как параметр
                    login=login,
                    email=email,
                    password=password
                )
            )
        return response

    def activate_registered_user(self, login: str):  # для получения токена из письма
        with allure.step("Активация пользователя"):
            token = self.facade.mailhog.get_token_by_login(login=login)  # переписали - теперь токен берется из письма по определенному пользователю
            response = self.facade.account_api.put_v1_account_token(
                token=token
            )
        return response

    def get_current_user_info(self, **kwargs):
        with allure.step("Получение данных пользователя"):
            response = self.facade.account_api.get_v1_account(**kwargs)
        return response

    def register_new_user_2(self, login: str, email: str, password: str, status_code: int):  # для дз по фикстурам добавил status_code
        with allure.step("Регистрация нового пользователя"):
            response = self.facade.account_api.post_v1_account(
                json=Registration(  # вынесли Registration не как модель, а как параметр
                    login=login,
                    email=email,
                    password=password
                ),
                status_code=status_code  # для дз по фикстурам добавил status_code
            )
        return response
