import requests
from services.dm_api_account import DmApiAccount


def test_put_v1_account_email():
    api = DmApiAccount(host='http://localhost:5051')
    json = {
        "login": "login1771",
        "email": "login1771@mail.ru",
        "password": "login1771login1771"
    }
    response = api.account.put_v1_account_email(
        json=json
    )
    print(response)


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

