from pydantic import BaseModel, StrictStr

# registration_model = {
#     "login": "login1771",
#     "email": "login1771@mail.ru",
#     "password": 1
# }


class RegistrationModel(BaseModel):
    login: StrictStr
    email: StrictStr
    password: StrictStr


# print(RegistrationModel(
#     login="True",
#     email="login1771@mail.ru",
#     password='1'
# ).json())
