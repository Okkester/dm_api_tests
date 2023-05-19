import requests
from services.dm_api_account import DmApiAccount
from services.mailhog import MailhogApi  # импорт чтобы брать данные из класса MailhogApi
import structlog
from dm_api_account.models.registration_model import Registration

structlog.configure(
    processors=[  # набор процессоров форматируют наш код в консоли. Процессоры лежат в либе structlog
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]  # параметры процессора: indent - отступ в джсоне, ensure_ascii=False - для работы с русской кодировкой
)


def test_post_v1_account():
    mailhog = MailhogApi(host="http://localhost:5025")
    api = DmApiAccount(host='http://localhost:5051')
    json = Registration(
        login='login177180001',
        email="login177180001@mail.ru",
        password='login170001'
    )
    # check_input_json(json=json)  # вызов функции для валидации джсон по типу данных
    response = api.account.post_v1_account(json=json)
    # token = mailhog.get_token_from_last_email()
    # response = api.account.put_v1_account_token(token=token)


# def check_input_json(json):
#     for key, value in json.items():  # валидация джсон по типу данных с помощью isinstance
#         if key == 'login':
#             assert isinstance(value, str), f'Тип значения в ключе {key} должен быть str, но получен {type(value)}'
#         elif key == 'email':
#             assert isinstance(value, str), f'Тип значения в ключе {key} должен быть str, но получен {type(value)}'
#         elif key == 'password':
#             assert isinstance(value, str), f'Тип значения в ключе {key} должен быть str, но получен {type(value)}'
# Но такая валидация не подходит для многоуровневых джсонов 01:00


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
