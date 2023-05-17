from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, StrictStr, Extra, Field
# pydantic - для валидации джсонов

# registration_model = {
#     "login": "login1771",
#     "email": "login1771@mail.ru",
#     "password": 1
# }


class Registration(BaseModel):
    class Config:
        extra = Extra.forbid

    login: Optional[StrictStr] = Field(None, description='Login')
    email: Optional[StrictStr] = Field(None, description='Email')
    password: Optional[StrictStr] = Field(None, description='Password')


# print(RegistrationModel(
#     login="True",
#     email="login1771@mail.ru",
#     password='1'
# ).json())
