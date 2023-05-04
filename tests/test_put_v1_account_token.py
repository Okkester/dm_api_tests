import requests
from services.dm_api_account import DmApiAccount


def test_put_v1_account_token():
    api = DmApiAccount(host='http://localhost:5051')
    token = '9a42e835-faa5-4e6b-aa3f-bd574e967411'
    response = api.account.put_v1_account_token(token)
    print(response)



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


