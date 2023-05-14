import requests
from requests import Response  # для поддержки возврата объекта response
from ..models.change_email_model import ChangeEmailModel
from ..models.change_password_model import ChangePasswordModel
from ..models.registration_model import RegistrationModel
from ..models.reset_password_model import ResetPasswordModel
from requests import session
from restclient.restclient import Restclient
from dm_api_account.models.user_envelope_model import UserEnvelopeModel
from dm_api_account.models.user_details_envelope_model import UserDetailsEnvelopeModel


class AccountApi:  # Это наш клиент
    def __init__(self, host, headers=None):
        self.host = host  # для того чтобы если урл изменится можно было его поменять в одном месте
        self.client = Restclient(host=host, headers=headers)  # нужно для того чтобы один раз авторизовавшись не прокидывать в заголовки токены постоянно
        if headers:
            self.client.session.headers.update(headers)  # обновление заголовков

    def post_v1_account(self, json: RegistrationModel, **kwargs) -> Response:  # для поддержки возврата объекта response
        """
         Register new user
        :param json registration_model
        :return:
        """
        response = self.client.post(  # self.session чтобы знать что все запросы будут выполняться в рамках одной сессии
            path=f"/v1/account",
            json=json.dict(by_alias=True, exclude_none=True),
            # раньше было равно payload, но payload перенесли в пакет models (registration_model).
            # Метод .dict() преобразовывает RegistrationModel в джсон
            # by_alias - параметр для использования именно тех алиасов которые указали
            # exclude_none - выключает поля, которые не обязательные
            **kwargs
        )
        return response

    def post_v1_account_password(self, json: ResetPasswordModel,
                                 **kwargs) -> Response:  # **kwargs - для передачи в функцию переменного кол-ва аргументов (заголовков)
        """
        Reset registered user password
        :param json: reset_password_model
        :return:
        """
        response = self.client.post(
            path=f"/v1/account/password",
            json=json.dict(by_alias=True, exclude_none=True),
            **kwargs  # с помощью **kwargs можно явно указать заголовки
        )
        UserEnvelopeModel(**response.json())
        return response

    def put_v1_account_email(self, json: ChangeEmailModel, **kwargs) -> Response:
        """
        Change registered user email
        :param json: change_email_model
        :return:
        """
        response = self.client.put(
            path=f"/v1/account/email",
            json=json.dict(by_alias=True, exclude_none=True),
            **kwargs
        )
        UserEnvelopeModel(**response.json())
        return response

    def put_v1_account_password(self, json: ChangePasswordModel, **kwargs) -> Response:
        """
        Change registered user password
        :param json: change_password_model
        :return:
        """
        response = self.client.put(
            path=f"/v1/account/password",
            json=json.dict(by_alias=True, exclude_none=True),
            **kwargs
        )
        UserEnvelopeModel(**response.json())
        return response

    def put_v1_account_token(self, token: str, **kwargs) -> Response:
        """
        Activate registered user
        :param token:
        :return:
        """

        response = self.client.put(
            path=f"/v1/account/{token}",
            **kwargs
        )
        UserEnvelopeModel(**response.json())  # две звёздочки ставятся для распаковки джсона, валидация джсона
        return response

    def get_v1_account(self, **kwargs) -> Response:
        """
        Get current user
        :return:
        """

        response = self.client.get(
            path=f"v1/account",
            **kwargs
        )
        UserDetailsEnvelopeModel(**response.json())
        return response
