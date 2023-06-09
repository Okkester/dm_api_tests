from services.dm_api_account import Facade
from hamcrest import assert_that, has_properties  # для сравнения ИЗБРАННЫХ полей с ожидаемыми полями в ответе
from apis.dm_api_account import UserRole
import structlog

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_put_v1_account_email():
    api = Facade(host='http://localhost:5051')
    json = {
        "login": "strsdfas0001",
        "email": "trf4f4f0002@mail.ru",
        "password": "stf4f0001"
    }
    response = api.account.put_v1_account_email(
        json=json,
        status_code=200
    )
    assert_that(response.resource, has_properties(  # проверка полей модели UserEnvelope
        {
            "login": "strsdfas0001",
            "roles": [UserRole.GUEST, UserRole.PLAYER]
        }
    ))




# def test_put_v1_account_email():
#     api = DmApiAccount(host='http://localhost:5051')
#     json = {
#         "login": "login1771",
#         "email": "login1771@mail.ru",
#         "password": "login1771login1771"
#     }
#     response = api.account.put_v1_account_email(
#         json=json
#     )
#     print(response)


# def put_v1_account_email():
#     """
#     Change registered user email
#     :return:
#     """
#     url = "http://localhost:5051/v1/account/email"
#
#     payload = {
#       "login": "<string>",
#       "password": "<string>",
#       "email": "<string>"
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
#       json=payload
#     )
#     return response
