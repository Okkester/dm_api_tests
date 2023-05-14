from pydantic import BaseModel, StrictStr


class ResetPasswordModel(BaseModel):
    login: StrictStr
    email: StrictStr

# reset_password_model = {
#     "login": "<string>",
#     "email": "<string>"
# }
