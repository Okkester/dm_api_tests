import requests
from requests import Response  # для поддержки возврата объекта response
from ..models import *
from requests import session
from restclient.restclient import Restclient
from dm_api_account.models.user_envelope_model import UserEnvelope
from dm_api_account.models.user_details_envelope_model import UserDetailsEnvelope
from dm_api_account.utilities import validate_request_json, validate_status_code


class AccountApi:  # Это наш клиент
    def __init__(self, host, headers=None):
        self.host = host  # для того чтобы если урл изменится можно было его поменять в одном месте
        self.client = Restclient(host=host, headers=headers)  # нужно для того чтобы один раз авторизовавшись не прокидывать в заголовки токены постоянно
        if headers:
            self.client.session.headers.update(headers)  # обновление заголовков

    def post_v1_account(
            self,
            json: Registration,
            status_code: int = 201,
            **kwargs
    ) -> Response:  # для поддержки возврата объекта response
        """
         Register new user
        :param status_code:
        :param json registration_model
        :return:
        """
        response = self.client.post(  # self.session чтобы знать что все запросы будут выполняться в рамках одной сессии
            path=f"/v1/account",
            json=validate_request_json(json),
            # раньше было равно payload, но payload перенесли в пакет models (registration_model).
            # Метод .dict() преобразовывает RegistrationModel в джсон
            # by_alias - параметр для использования именно тех алиасов которые указали
            # exclude_none - выключает поля, которые не обязательные
            **kwargs
        )
        validate_status_code(response, status_code)
        return response

    def post_v1_account_password(
            self,
            json: ResetPassword,
            status_code: int = 200,
            **kwargs
    ) -> Response | UserEnvelope:
        # **kwargs - для передачи в функцию переменного кол-ва аргументов (заголовков)
        """
        Reset registered user password
        :param status_code:
        :param json: reset_password_model
        :return:
        """
        response = self.client.post(
            path=f"/v1/account/password",
            json=validate_request_json(json),
            **kwargs
        )
        validate_status_code(response, status_code)
        if response.status_code == 201:
            return UserEnvelope(**response.json())  # две звёздочки ставятся для распаковки джсона, валидация джсона
        return response

    def put_v1_account_email(
            self,
            json: ChangeEmail,
            status_code: int,
            **kwargs
    ) -> Response | UserEnvelope:
        """
        Change registered user email
        :param status_code:
        :param json: change_email_model
        :return:
        """
        response = self.client.put(
            path=f"/v1/account/email",
            json=validate_request_json(json),
            **kwargs
        )
        validate_status_code(response, status_code)
        if response.status_code == 200:
            return UserEnvelope(**response.json())
        return response

    def put_v1_account_password(
            self,
            json: ChangePassword,
            status_code: int,
            **kwargs
    ) -> Response | UserEnvelope:
        """
        Change registered user password
        :param status_code:
        :param json: change_password_model
        :return:
        """
        response = self.client.put(
            path=f"/v1/account/password",
            json=validate_request_json(json),
            **kwargs
        )
        validate_status_code(response, status_code)
        if response.status_code == 200:
            return UserEnvelope(**response.json())
        return response

    def put_v1_account_token(
            self,
            token: str,
            status_code: int = 200,
            **kwargs
    ) -> Response | UserEnvelope:
        """
        Activate registered user
        :param status_code:
        :param token:
        :return:
        """

        response = self.client.put(
            path=f"/v1/account/{token}",
            **kwargs
        )
        validate_status_code(response, status_code)
        if response.status_code == 200:
            return UserEnvelope(**response.json())
        return response

    def get_v1_account(
            self,
            status_code: int = 200,  # добавил на 08:16
            **kwargs
    ) -> Response | UserDetailsEnvelope:
        """
        Get current user
        :return:
        """

        response = self.client.get(
            path=f"/v1/account",
            **kwargs
        )
        validate_status_code(response, status_code)
        if response.status_code == 200:
            return UserDetailsEnvelope(**response.json())
        return response
