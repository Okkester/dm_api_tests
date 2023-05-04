import requests
from services.dm_api_account import DmApiAccount


def test_post_v1_account():
    api = DmApiAccount(host='http://localhost:5051')
    json = {
        "login": "login17712",
        "email": "login17712@mail.ru",
        "password": "login17712login17712"
    }
    response = api.account.post_v1_account(
        json=json
    )
    print(response)
# import requests
#
#
# def post_v1_account():
#     """
#     Register new user
#     :return:
#     """
#     url = "http://localhost:5051/v1/account"
#
#     payload = {
#         "login": "login1771",
#         "email": "login1771@mail.ru",
#         "password": "login1771login1771"
#     }
#     headers = {
#         'X-Dm-Auth-Token': '<string>',
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
#
#
# response = post_v1_account()
#
# # свойства ответа:
# print(response.content)
# print(response.url)
# print(response.status_code)
# print(response.json())
#
# # свойства запроса
# print(response.request.url)
# print(response.request.method)
# print(response.request.headers)
# print(response.request.body)
