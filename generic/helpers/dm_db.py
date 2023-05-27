from db_client.db_client import DbClient


class DmDatabase:
    def __init__(self, user, password, host, database):
        self.db = DbClient(user, password, host, database)  # параметр из под которого выполняются запросы

    def get_all_users(self):  # обёртка в которой прикручено логирование
        query = 'select * from "public"."Users"'
        dataset = self.db.send_query(query=query)
        return dataset

    def get_user_by_login(self, login):  # получение юзера по его логину
        query = f'''
        select * from "public"."Users"
        where "Login" = '{login}'
        '''
        dataset = self.db.send_query(query=query)
        return dataset

    def delete_user_by_login(self, login):  # удаление юзера по его логину
        query = f'''
        delete from "public"."Users"
        where "Login" = '{login}'
        '''
        dataset = self.db.send_bulk_query(query=query)
        return dataset

    # ДЗ
    def update_activated_status_user_by_login(self, login):  # смена признака активации на true
        query = f'''
        update "public"."Users"
        set "Activated" = 'true'
        where "public"."Users"."Login" = '{login}'
        '''
        dataset = self.db.send_bulk_query(query=query)
        return dataset
