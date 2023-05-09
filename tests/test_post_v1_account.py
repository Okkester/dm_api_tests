import requests
from services.dm_api_account import DmApiAccount
from services.mailhog import MailhogApi  # импорт чтобы брать данные из класса MailhogApi
import structlog

structlog.configure(
    processors=[  # набор процессоров форматируют наш код в консоли. Процессоры лежат в либе structlog
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]  # параметры процессора: indent - отступ в джсоне, ensure_ascii=False - для работы с русской кодировкой
)


def test_post_v1_account():
    mailhog = MailhogApi(host="http://localhost:5025")
    api = DmApiAccount(host='http://localhost:5051')
    json = {
        "login": "login177182",
        "email": "login177182@mail.ru",
        "password": "login177182login17715"
    }
    response = api.account.post_v1_account(json=json)
    assert response.status_code == 201, f'Статус код ответа должен быть равен 201, но он равен {response.status_code}'
    token = mailhog.get_token_from_last_email()
    response = api.account.put_v1_account_token(token=token)


# import requests
#
#
# def post_v1_account():
#     """
#     Register new user
#     :return:
#     """
#     url = "http://localhost:5051/v1/account"
#
#     payload = {
#         "login": "login1771",
#         "email": "login1771@mail.ru",
#         "password": "login1771login1771"
#     }
#     headers = {
#         'X-Dm-Auth-Token': '<string>',
#         'X-Dm-Bb-Render-Mode': '<string>',
#         'Content-Type': 'application/json',
#         'Accept': 'text/plain'
#     }
#
#     response = requests.request(
#         method="POST",
#         url=url,
#         headers=headers,
#         json=payload
#     )
#     return response
#
#
# response = post_v1_account()
#
# # свойства ответа:
# print(response.content)
# print(response.url)
# print(response.status_code)
# print(response.json())
#
# # свойства запроса
# print(response.request.url)
# print(response.request.method)
# print(response.request.headers)
# print(response.request.body)
