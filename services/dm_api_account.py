from dm_api_account.apis.account_api import AccountApi
from dm_api_account.apis.login_api import LoginApi
from generic.helpers.mailhog import MailhogApi
from generic.helpers.account import Account
from generic.helpers.login import Login


class Facade:  # класс фасад, который будет обвязывать всех помощников для удобного доступа
    def __init__(self, host, mailhog=None, headers=None):
        self.account_api = AccountApi(host, headers)
        self.login_api = LoginApi(host, headers)
        self.mailhog = mailhog  # сюда передаём фикстуру
        self.account = Account(
            self)  # self даёт доступ ко всем методам и свойствам которые описаны в этом классе для удобства написания обертки в helpers
        self.login = Login(self)  # self даёт доступ ко всем методам и свойствам которые описаны в этом классе

# class Facade:  # класс фасад, который будет обвязывать всех помощников для удобного доступа
#     def __init__(self, host, mailhog=None, headers=None):
#         self.account_api = AccountApi(host, headers)
#         self.login_api = LoginApi(host, headers)
#         self.mailhog = MailhogApi()
#         self.account = Account(self)  # self даёт доступ ко всем методам и свойствам которые описаны в этом классе для удобства написания обертки в helpers
#         self.login = Login(self)  # self даёт доступ ко всем методам и свойствам которые описаны в этом классе
