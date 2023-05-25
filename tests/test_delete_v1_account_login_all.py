import requests
from services.dm_api_account import Facade
import structlog

structlog.configure(
    processors=[  # набор процессоров форматируют наш код в консоли. Процессоры лежат в либе structlog
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]  # параметры процессора: indent - отступ в джсоне, ensure_ascii=False - для работы с русской кодировкой
)


def test_delete_v1_account_login_all():
    api = Facade(host='http://localhost:5051')  # инициализация
    # register new user
    login = 'strtest5'  # завели три переменные для регистрации->активации->авторизации
    email = 'strtest5@mail.ru'
    password = 'strtest5'
    response = api.account.register_new_user(  # прописали обёртку над методом из helpers Account
        login=login,
        email=email,
        password=password
    )
    # activate  user
    api.account.activate_registered_user(
        login=login)  # прописали обёртку над методом put_v1_account_token из helpers Account

    # Login  user
    api.login.login_user(
        login=login,
        password=password
    )

    # Logout  user - ДЗ - Разлогиниться при помощи установки авторизационных заголовков в клиент
    token = api.login.get_auth_token(login='strtest5',
                                     password='strtest5')  # возвращает авторизационный токен X-Dm-Auth-Token
    api.login.set_headers(headers=token)
    api.login.logout_user_from_all_devices()

# def test_delete_v1_account_login_all():
#     api = Facade(host='http://localhost:5051')
#     headers = {
#         'X-Dm-Auth-Token': 'IQJh+zgzF5C6aD9mqQUFu7UTPKMLiqANOWWewewAMIx2UXGllRCZPOE0syF8v/f0kAna2FA+uJbiLt7M+Bdw63XkHoWleSEOJlUYZ75G6s2sELNs59Fbf9lAIkokrzQoZyeZ/Lqqa2w=',
#         'X-Dm-Bb-Render-Mode': '<string>',
#         'Accept': 'text/plain'
#     }
#     response = api.login.delete_v1_account_login_all(
#         headers=headers
#     )


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
