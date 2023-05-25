import requests
from services.dm_api_account import Facade
import structlog

structlog.configure(
    processors=[  # набор процессоров форматируют наш код в консоли. Процессоры лежат в либе structlog
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]  # параметры процессора: indent - отступ в джсоне, ensure_ascii=False - для работы с русской кодировкой
)


def test_get_v1_account():
    api = Facade(host='http://localhost:5051')
    token = api.login.get_auth_token(login='strtest1', password='strtest1')  # получение токена X-Dm-Auth-Token
    api.account.set_headers(headers=token)  # устанока заголовков (токена) в клиент в аккаунт
    api.login.set_headers(headers=token)  # устанока заголовков (токена) в клиент в логин

    api.account.get_current_user_info()  # для получения информации о пользователе
    # api.login.logout_user()  # логаут
    api.login.logout_user_from_all_devices()  # логаут со всех устройств




# from services.dm_api_account import Facade
# from hamcrest import assert_that, has_properties  # для сравнения ИЗБРАННЫХ полей с ожидаемыми полями в ответе
# from dm_api_account.models.user_details_envelope_model import UserRole
# import structlog
#
# structlog.configure(
#     processors=[
#         structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
#     ]
# )
#
#
# def test_get_v1_account():
#     api = Facade(host='http://localhost:5051')
#     headers = {
#         'X-Dm-Auth-Token': 'IQJh+zgzF5DOuBBWRs9shMXToTcuU+Q4OvbgTPgLWKHHrqeXocd5s9k4pm7ssjUJQ3RGXJcy6PFWyzoktuLbIX5vKPKHXvrvIq/Bqp/iJrHe0OTpBZcuPXmZ7XFk2q9hyiJajqpVdDw=',
#         'X-Dm-Bb-Render-Mode': '<string>',
#         'Accept': 'text/plain'
#     }
#     response = api.account.get_v1_account(
#         headers=headers,
#         status_code=200
#     )
#     assert_that(response.resource, has_properties(  # проверка полей модели UserEnvelope
#         {
#             "login": "login177180001",
#             "roles": [UserRole.GUEST, UserRole.PLAYER]
#         }
#     ))


# def test_get_v1_account():
#     api = DmApiAccount(host='http://localhost:5051')
#     headers = {
#         'X-Dm-Auth-Token': '<string>',
#         'X-Dm-Bb-Render-Mode': '<string>',
#         'Accept': 'text/plain'
#     }
#     response = api.account.get_v1_account(
#         headers=headers
#     )
#     print(response)


# def get_v1_account():
#     """
#     Get current user
#     :return:
#     """
#     url = "http://localhost:5051/v1/account"
#
#     payload = {}
#     headers = {
#       'X-Dm-Auth-Token': '<string>',
#       'X-Dm-Bb-Render-Mode': '<string>',
#       'Accept': 'text/plain'
#     }
#
#     response = requests.request(
#         method="GET",
#         url=url,
#         headers=headers,
#         json=payload
#     )
#     return response
