from services.dm_api_account import Facade
import structlog

structlog.configure(
    processors=[  # набор процессоров форматируют наш код в консоли. Процессоры лежат в либе structlog
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]  # параметры процессора: indent - отступ в джсоне, ensure_ascii=False - для работы с русской кодировкой
)


def test_post_v1_account():
    api = Facade(host='http://localhost:5051')  # инициализация
    # register new user
    login = 'strtest6'    # завели три переменные для регистрации->активации->авторизации
    email = 'strtest6@mail.ru'
    password = 'strtest6'
    response = api.account.register_new_user(  # прописали обёртку над методом из helpers Account
        login=login,
        email=email,
        password=password
    )
    # activate  user
    api.account.activate_registered_user(login=login)  # прописали обёртку над методом put_v1_account_token из helpers Account

    # Login  user
    api.login.login_user(
        login=login,
        password=password
    )

    # Logout  user - ДЗ - Разлогиниться  при передаче заголовков в метод через **kwargs
    token = api.login.get_auth_token(login='strtest6', password='strtest6')    # возвращает авторизационный токен X-Dm-Auth-Token
    api.login_api.delete_v1_account_login(headers=token)


    # # Logout  user - ДЗ - Разлогиниться при помощи установки авторизационных заголовков в клиент
    # token = api.login.get_auth_token(login='strtest4', password='strtest4')    # возвращает авторизационный токен X-Dm-Auth-Token
    # api.login.set_headers(headers=token)
    # api.login.logout_user()
