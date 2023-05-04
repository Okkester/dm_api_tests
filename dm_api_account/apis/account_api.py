import requests
from requests import Response  # для поддержки возврата объекта response
from ..models.change_email_model import change_email_model
from ..models.change_password_model import change_password_model
from ..models.registration_model import registration_model
from ..models.reset_password_model import reset_password_model
from requests import session


class AccountApi:
    def __init__(self, host, headers=None):
        self.host = host     # для того чтобы если урл изменится можно было его поменять в одном месте
        self.session = session()  # нужно для того чтобы один раз авторизовавшись не прокидывать в заголовки тоены постоянно
        if headers:
            self.session.headers.update(headers)     # обновление заголовков

    def post_v1_account(self, json: registration_model, **kwargs) -> Response:  # для поддержки возврата объекта response
        """
         Register new user
        :param json registration_model
        :return:
        """
        response = self.session.post(        # self.session чтобы знать что все запросы будут выполняться в рамках одной сессии
            url=f"{self.host}/v1/account",
            json=json,   #раньше было равно payload, но payload перенесли в пакет models (registration_model)
            **kwargs
        )
        return response

    def post_v1_account_password(self, json: reset_password_model, **kwargs) -> Response:  # **kwargs - для передачи в функцию переменного кол-ва аргументов (заголовков)
        """
        Reset registered user password
        :param json: reset_password_model
        :return:
        """
        response = self.session.post(
            url=f"{self.host}/v1/account/password",
            json=json,
            **kwargs  # с помощью **kwargs можно явно указать заголовки
        )
        return response

    def put_v1_account_email(self, json: change_email_model, **kwargs) -> Response:
        """
        Change registered user email
        :param json: change_email_model
        :return:
        """
        response = self.session.put(
            url=f"{self.host}/v1/account/email",
            json=json,
            **kwargs
        )
        return response

    def put_v1_account_password(self, json: change_password_model, **kwargs) -> Response:
        """
        Change registered user password
        :param json: change_password_model
        :return:
        """
        response = self.session.put(
            url=f"{self.host}/v1/account/password",
            json=json,
            **kwargs
        )
        return response

    def put_v1_account_token(self, token: str, **kwargs) -> Response:
        """
        Activate registered user
        :param token:
        :return:
        """

        headers = {
            'X-Dm-Auth-Token': '<string>',
            'X-Dm-Bb-Render-Mode': '<string>',
            'Accept': 'text/plain'
        }

        response = self.session.put(
            url=f"{self.host}/v1/account/{token}",
            headers=headers,
            **kwargs
        )
        return response

    def get_v1_account(self, **kwargs) -> Response:
        """
        Get current user
        :return:
        """
        headers = {
                  'X-Dm-Auth-Token': '<string>',
                  'X-Dm-Bb-Render-Mode': '<string>',
                  'Accept': 'text/plain'
                }

        response = self.session.get(
            url=f"{self.host}v1/account",
            headers=headers,
            **kwargs
        )
        return response
