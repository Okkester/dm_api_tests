from typing import List
from sqlalchemy import select, delete
from generic.helpers.orm_models import Users
from orm_client.orm_client import OrmClient
import allure


class OrmDatabase:  # описание orm-клиента
    def __init__(self, user, password, host, database):
        self.db = OrmClient(user, password, host, database)  # параметр из под которого выполняются запросы

    def get_all_users(self):  # обёртка в которой прикручено логирование
        with allure.step("Запрос в БД для получения всех пользователей"):
            query = select([Users])  # выполнение запроса
            dataset = self.db.send_query(query)
        return dataset

    def get_user_by_login(self, login) -> List[Users]:  # обёртка в которой прикручено логирование
        with allure.step("Запрос в БД для получения пользователя по его логину"):
            query = select([Users]).where(
                Users.Login == login
            )
            dataset = self.db.send_query(query)
        return dataset

    def delete_user_by_login(self, login) -> List[Users]:  # удаление юзера по его логину
        with allure.step("Запрос в БД для удаления пользователя по его логину"):
            query = delete(Users).where(
                Users.Login == login
            )
            dataset = self.db.send_bulk_query(query)
        return dataset
