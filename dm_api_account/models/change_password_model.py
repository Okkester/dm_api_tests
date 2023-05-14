from pydantic import BaseModel, StrictStr


class ChangePasswordModel(BaseModel):
    login: StrictStr
    token: StrictStr
    oldPassword: StrictStr
    newPassword: StrictStr

# change_password_model = {
#     "login": "<string>",
#     "token": "<uuid>",
#     "oldPassword": "<string>",
#     "newPassword": "<string>"
# }
