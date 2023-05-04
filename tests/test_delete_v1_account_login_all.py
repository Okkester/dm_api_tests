import requests
from services.dm_api_account import DmApiAccount


def test_delete_v1_account_login_all():
    api = DmApiAccount(host='http://localhost:5051')
    headers = {
        'X-Dm-Auth-Token': '<string>',
        'X-Dm-Bb-Render-Mode': '<string>',
        'Accept': 'text/plain'
    }
    response = api.account.delete_v1_account_login_all(
        headers=headers
    )
    print(response)

# def delete_v1_account_login_all():
#     """
#     Logout from every device
#     :return:
#     """
#     url = "http://localhost:5051/v1/account/login/all"
#
#     payload = {}
#     headers = {
#       'X-Dm-Auth-Token': '<string>',
#       'X-Dm-Bb-Render-Mode': '<string>',
#       'Accept': 'text/plain'
#     }
#
#     response = requests.request(
#         method="DELETE",
#         url=url,
#         headers=headers,
#         json=payload
#     )
#     return response

