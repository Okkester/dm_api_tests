import requests

from services.dm_api_account import DmApiAccount
from hamcrest import assert_that, has_properties  # для сравнения ИЗБРАННЫХ полей с ожидаемыми полями в ответе
from dm_api_account.models.user_details_envelope_model import UserRole
import structlog

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_get_v1_account():
    api = DmApiAccount(host='http://localhost:5051')
    headers = {
        'X-Dm-Auth-Token': '<string>',
        'X-Dm-Bb-Render-Mode': '<string>',
        'Accept': 'text/plain'
    }
    response = api.account.get_v1_account(
        headers=headers,
        status_code=200
    )
    assert_that(response.resource, has_properties(  # проверка полей модели UserEnvelope
        {
            "login": "login17712",
            "roles": [UserRole.GUEST, UserRole.PLAYER]
        }
    ))

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


