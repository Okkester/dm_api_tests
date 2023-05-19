import requests
from services.dm_api_account import DmApiAccount
import json
from hamcrest import assert_that, has_properties  # для сравнения ИЗБРАННЫХ полей с ожидаемыми полями в ответе
from dm_api_account.models.user_envelope_model import UserRole
# from services.mailhog import MailhogApi  # импорт чтобы брать данные из класса MailhogApi
import structlog

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_put_v1_account_token():
    api = DmApiAccount(host='http://localhost:5051')
    response = api.account.put_v1_account_token(token='d6346921-ced2-4f58-bdd0-067899cdd57b', status_code=200)
    assert_that(response.resource, has_properties(  # проверка полей модели UserEnvelope
        {
            "login": "login177180001",
            "roles": [UserRole.GUEST, UserRole.PLAYER]
        }
    ))





    # expected_json = {'resource': {
    #     "login": "doctest0004",
    #     "rating": {
    #         "enabled": True,
    #         "quality": 0,
    #         "quantity": 0
    #     },
    #     "roles": [
    #         "Guest",
    #         "Player"
    #     ],
    # }}
    # actual_json = json.loads(response.json(by_alias=True, exclude_none=True))
    # assert actual_json == expected_json

# def put_v1_account_token():
#     """
#     Activate registered user
#     :return:
#     """
#     token = '123412341235'
#     url = f"http://localhost:5051/v1/account/{token}"
#
#     payload = {}
#     headers = {
#         'X-Dm-Auth-Token': '<string>',
#         'X-Dm-Bb-Render-Mode': '<string>',
#         'Accept': 'text/plain'
#     }
#
#     response = requests.request(
#         method="PUT",
#         url=url,
#         headers=headers,
#         data=payload
#     )
#     return response
