from pydantic import BaseModel, StrictStr, StrictBool


class LoginCredentialsModel(BaseModel):
    login: StrictStr
    password: StrictStr
    rememberMe: StrictBool

# login_credentials_model = {
#     "login": "<string>",
#     "password": "<string>",
#     "rememberMe": False
# }
