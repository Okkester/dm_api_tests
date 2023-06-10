import requests
from services.dm_api_account import Facade
import structlog

structlog.configure(
    processors=[  # набор процессоров форматируют наш код в консоли. Процессоры лежат в либе structlog
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]  # параметры процессора: indent - отступ в джсоне, ensure_ascii=False - для работы с русской кодировкой
)


def test_delete_v1_account_login():
    api = Facade(host='http://localhost:5051')
    headers = {
        'X-Dm-Auth-Token': 'IQJh+zgzF5CxxHL33YAKoWKA1d19mtnsx0L5VaTJCq7M9j+kq8gjX0MEsov8KlJlSt5sgbe4uE/atl9vHePOYgCX5TdTfwF4SueurWKj47NYxtGDbps/4ULTcHDETylRv6AL4raUXo0=',
        'X-Dm-Bb-Render-Mode': '<string>',
        'Accept': 'text/plain'
    }
    response = api.login.delete_v1_account_login(
        headers=headers
    )




# def test_delete_v1_account_login():
#     api = DmApiAccount(host='http://localhost:5051')
#     headers = {
#         'X-Dm-Auth-Token': 'IQJh+zgzF5CxxHL33YAKoWKA1d19mtnsx0L5VaTJCq7M9j+kq8gjX0MEsov8KlJlSt5sgbe4uE/atl9vHePOYgCX5TdTfwF4SueurWKj47NYxtGDbps/4ULTcHDETylRv6AL4raUXo0=',
#         'X-Dm-Bb-Render-Mode': '<string>',
#         'Accept': 'text/plain'
#     }
#     response = api.account.delete_v1_account_login(
#         headers=headers
#     )
#     print(response)


# def delete_v1_account_login():
#     """
#     Logout as current user
#     :return:
#     """
#     url = "http://localhost:5051/v1/account/login"
#
#     headers = {
#         'X-Dm-Auth-Token': '<string>',
#         'X-Dm-Bb-Render-Mode': '<string>',
#         'Accept': 'text/plain'
#     }
#
#     response = requests.request(
#         method="DELETE",
#         url=url,
#         headers=headers
#     )
#     return response
