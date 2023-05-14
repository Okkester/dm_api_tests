from pydantic import BaseModel, StrictStr


class ChangeEmailModel(BaseModel):
    login: StrictStr
    email: StrictStr
    password: StrictStr

# change_email_model = {
#     "login": "login1771",
#     "email": "login1771@mail.ru",
#     "password": "login1771login1771"
# }
