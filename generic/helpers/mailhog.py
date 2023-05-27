import json
import time

from requests import session, Response
from restclient.restclient import Restclient


def decorator(fn):
    def wrapper(*args, **kwargs):  # обёртка
        for i in range(5):
            response = fn(*args, **kwargs)
            emails = response.json()['items']
            if len(emails) < 1:
                print(f'attempt {i}')
                time.sleep(2)
                continue
            else:
                return response

    return wrapper


class MailhogApi:
    def __init__(self, host="http://localhost:5025"):
        self.host = host  # на случай если урл-адрес переедет зашиваем его тут по умолчанию
        self.client = Restclient(
            host=host)  # заменили библиотеку requests на нашу библиотеку с логгированием, которая является оберткой над реквестс

    # @decorator
    def get_api_v2_messages(self, limit: int = 50) -> Response:
        """
        Get messages by limit
        :param limit:
        :return:
        """
        url = f"{self.host}/api/v2/messages?limit=50"

        response = self.client.get(  # заменили библиотеку requests на self.session
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

    def get_token_by_login(self, login: str, attempt=50):  # для получения письма от определенного пользователя
        if attempt == 0:
            raise AttributeError(f'Не удалось получить письмо с логином {login}')
        emails = self.get_api_v2_messages(limit=100).json()['items']
        for email in emails:
            user_data = json.loads(email['Content']['Body'])
            if login == user_data.get('Login'):
                token = user_data['ConfirmationLinkUrl'].split('/')[-1]
                # print(token)
                return token
            time.sleep(2)
            # print('Попытка получить письмо')
            return self.get_token_by_login(login=login, attempt=attempt - 1)

    # if __name__ == '__main__':
    #     MailhogApi().get_api_v2_messages(limit=50)

    def delete_all_messages(self):
        response = self.client.delete(path='/api/v1/messages')
        return response
