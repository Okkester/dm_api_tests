import requests
from services.dm_api_account import Facade
import structlog

structlog.configure(
    processors=[  # набор процессоров форматируют наш код в консоли. Процессоры лежат в либе structlog
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]  # параметры процессора: indent - отступ в джсоне, ensure_ascii=False - для работы с русской кодировкой
)


def test_delete_v1_account_login_all():
    api = Facade(host='http://localhost:5051')
    headers = {
        'X-Dm-Auth-Token': 'IQJh+zgzF5C6aD9mqQUFu7UTPKMLiqANOWWewewAMIx2UXGllRCZPOE0syF8v/f0kAna2FA+uJbiLt7M+Bdw63XkHoWleSEOJlUYZ75G6s2sELNs59Fbf9lAIkokrzQoZyeZ/Lqqa2w=',
        'X-Dm-Bb-Render-Mode': '<string>',
        'Accept': 'text/plain'
    }
    response = api.login.delete_v1_account_login_all(
        headers=headers
    )



# def test_delete_v1_account_login_all():
#     api = DmApiAccount(host='http://localhost:5051')
#     headers = {
#         'X-Dm-Auth-Token': '<string>',
#         'X-Dm-Bb-Render-Mode': '<string>',
#         'Accept': 'text/plain'
#     }
#     response = api.account.delete_v1_account_login_all(
#         headers=headers
#     )
#     print(response)


# def delete_v1_account_login_all():
#     """
#     Logout from every device
#     :return:
#     """
#     url = "http://localhost:5051/v1/account/login/all"
#
#     payload = {}
#     headers = {
#       'X-Dm-Auth-Token': '<string>',
#       'X-Dm-Bb-Render-Mode': '<string>',
#       'Accept': 'text/plain'
#     }
#
#     response = requests.request(
#         method="DELETE",
#         url=url,
#         headers=headers,
#         json=payload
#     )
#     return response
