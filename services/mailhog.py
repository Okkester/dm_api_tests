import json
from requests import session, Response
from restclient.restclient import Restclient


class MailhogApi:
    def __init__(self, host="http://localhost:5025"):
        self.host = host  # на случай если урл-адрес переедет зашиваем его тут по умолчанию
        self.client = Restclient(host=host)  # заменили библиотеку requests на нашу библиотеку с логгированием, которая является оберткой над реквестс

    def get_api_v2_messages(self, limit: int = 50) -> Response:
        """
        Get messages by limit
        :param limit:
        :return:
        """
        url = f"{self.host}/api/v2/messages?limit=50"

        response = self.client.get(       # заменили библиотеку requests на self.session
            path=f"/api/v2/messages",
            params={
                'limit': limit
            }
        )

        return response

    def get_token_from_last_email(self) -> str:  # если тест выше выполнился , то из него мы будем брать токен
        """
        Get user activation token from last email
        :return:
        """
        emails = self.get_api_v2_messages(limit=1).json()  # .json нужно для преобразования в джсон
        token_url = json.loads(emails['items'][0]['Content']['Body'])[
            'ConfirmationLinkUrl']  # json.loads преобразовывает строку в Body в словарь
        token = token_url.split('/')[
            -1]  # разбиваем строку token_url по символу / и получаем список. В списке обращаемся к последнему элементу
        return token
