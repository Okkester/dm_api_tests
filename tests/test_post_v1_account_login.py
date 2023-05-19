import requests
from services.dm_api_account import DmApiAccount
from hamcrest import assert_that, has_properties  # для сравнения ИЗБРАННЫХ полей с ожидаемыми полями в ответе
from dm_api_account.models.user_envelope_model import UserRole
import structlog

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_post_v1_account_login():
    api = DmApiAccount(host='http://localhost:5051')
    json = {
        "login": "login177180001",
        "password": "login170001",
        "rememberMe": False
    }
    response = api.login.post_v1_account_login(
        json=json,
        status_code=200
    )
    assert_that(response.resource, has_properties(  # проверка полей модели UserEnvelope
        {
            "login": "login177180001",
            "roles": [UserRole.GUEST, UserRole.PLAYER]
        }
    ))




# def test_post_v1_account_login():
#     api = DmApiAccount(host='http://localhost:5051')
#     json = {
#         "login": "<string>",
#         "password": "<string>",
#         "rememberMe": False
#     }
#     response = api.account.post_v1_account_login(
#         json=json
#     )
#     print(response)

# def post_v1_account_login():
#     """
#     Authenticate via credentials
#     :return:
#     """
#     url = "http://localhost:5051/v1/account/login"
#
#     payload = {
#         "login": "<string>",
#         "password": "<string>",
#         "rememberMe": "<boolean>"
#     }
#     headers = {
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
