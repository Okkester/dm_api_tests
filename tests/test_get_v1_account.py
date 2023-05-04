import requests

from services.dm_api_account import DmApiAccount


def test_get_v1_account():
    api = DmApiAccount(host='http://localhost:5051')
    headers = {
        'X-Dm-Auth-Token': '<string>',
        'X-Dm-Bb-Render-Mode': '<string>',
        'Accept': 'text/plain'
    }
    response = api.account.get_v1_account(
        headers=headers
    )
    print(response)


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


