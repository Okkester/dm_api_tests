from dm_api_account.models import Registration


class Account:  # отвечает за регистрацию и активацию юзера
    def __init__(self, facade): # в параметр facade будет приходить класс Facade
        self.facade = facade

    # ниже функции описывают обёртки над методами
    def set_headers(self, headers):  # установка заголовков в клиент
        self.facade.account_api.client.session.headers.update(headers)

    def register_new_user(self, login: str, email: str, password: str):
        response = self.facade.account_api.post_v1_account(
            json=Registration(  # вынесли Registration не как модель, а как параметр
                login=login,
                email=email,
                password=password
            )
        )
        return response

    def activate_registered_user(self, login: str):  # для получения токена из письма
        token = self.facade.mailhog.get_token_by_login(login=login)  # переписали - теперь токен берется из письма по определенному пользователю
        response = self.facade.account_api.put_v1_account_token(
            token=token
        )
        return response

    def get_current_user_info(self, **kwargs):
        response = self.facade.account_api.get_v1_account(**kwargs)
        return response
