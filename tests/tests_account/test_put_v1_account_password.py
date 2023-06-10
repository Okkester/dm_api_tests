from services.dm_api_account import Facade
from hamcrest import assert_that, has_properties  # для сравнения ИЗБРАННЫХ полей с ожидаемыми полями в ответе
from apis.dm_api_account import UserRole
import structlog

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_put_v1_account_password():
    api = Facade(host='http://localhost:5051')
    json = {
        "login": "strsdfas0001",
        "token": "4a680634-96db-4e31-a209-778353c7bc08",
        "oldPassword": "stf4f0001",
        "newPassword": "stf4f0002"
    }
    response = api.account.put_v1_account_password(
        json=json,
        status_code=200
    )
    assert_that(response.resource, has_properties(  # проверка полей модели UserEnvelope
        {
            "login": "login17713",
            "roles": [UserRole.GUEST, UserRole.PLAYER]
        }
    ))



# def test_put_v1_account_password():
#     api = DmApiAccount(host='http://localhost:5051')
#     json = {
#         "login": "<string>",
#         "token": "<uuid>",
#         "oldPassword": "<string>",
#         "newPassword": "<string>"
#     }
#     response = api.account.put_v1_account_password(
#         json=json
#     )
#     print(response)


# def put_v1_account_password():
#     """
#     Change registered user password
#     :return:
#     """
#     url = "http://localhost:5051/v1/account/password"
#
#     payload = {
#       "login": "<string>",
#       "token": "<uuid>",
#       "oldPassword": "<string>",
#       "newPassword": "<string>"
#     }
#     headers = {
#       'X-Dm-Auth-Token': '<string>',
#       'X-Dm-Bb-Render-Mode': '<string>',
#       'Content-Type': 'application/json',
#       'Accept': 'text/plain'
#     }
#
#     response = requests.request(
#       method="PUT",
#       url=url,
#       headers=headers,
#       data=payload
#     )
#     return response
