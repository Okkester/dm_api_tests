import requests
from services.dm_api_account import DmApiAccount


def test_put_v1_account_password():
    api = DmApiAccount(host='http://localhost:5051')
    json = {
        "login": "<string>",
        "token": "<uuid>",
        "oldPassword": "<string>",
        "newPassword": "<string>"
    }
    response = api.account.put_v1_account_password(
        json=json
    )
    print(response)


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


