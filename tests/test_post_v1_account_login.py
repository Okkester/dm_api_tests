import requests
from services.dm_api_account import DmApiAccount


def test_post_v1_account_login():
    api = DmApiAccount(host='http://localhost:5051')
    json = {
        "login": "<string>",
        "password": "<string>",
        "rememberMe": False
    }
    response = api.account.post_v1_account_login(
        json=json
    )
    print(response)


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
