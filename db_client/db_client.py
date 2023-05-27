import records
import structlog
import uuid

structlog.configure(
    processors=[  # набор процессоров форматируют наш код в консоли. Процессоры лежат в либе structlog
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]  # параметры процессора: indent - отступ в джсоне, ensure_ascii=False - для работы с русской кодировкой
)


class DbClient:  # обёртка логирующая запросы
    def __init__(self, user, password, host, database, isolation_level='AUTOCOMMIT'):
        connection_string = f'postgresql://{user}:{password}@{host}/{database}'  # для подключения к БД
        self.db = records.Database(connection_string, isolation_level=isolation_level)  # параметр из под которого выполняются запросы
        self.log = structlog.get_logger(self.__class__.__name__).bind(service='db')  # создали логгер

    def send_query(self, query):  # метод-обёртка, который будет логировать запрос
        print(query)  # query - строка с sql-запросом
        log = self.log.bind(event_id=str(uuid.uuid4()))  # сделали также как в restclient для хранения event_id
        log.msg(  # формирование логирующего сообщения
            event='request',  # запрос в БД
            query=query  # сюда выводится запрос
        )
        dataset = self.db.query(query=query).as_dict()  # возвращаемый датасет в виде словаря
        log.msg(  # логирование полученного датасета
            event='response',
            dataset=dataset
        )
        return dataset

    def send_bulk_query(self, query):  # метод-обёртка, который будет логировать запрос
        print(query)  # query - строка с sql-запросом
        log = self.log.bind(event_id=str(uuid.uuid4()))  # сделали также как в restclient для хранения event_id
        log.msg(  # формирование логирующего сообщения
            event='request',  # запрос в БД
            query=query  # сюда выводится запрос
        )
        self.db.bulk_query(query=query)  # возвращаемый датасет в виде словаря



# if __name__ == '__main__':
#     db = DbClient(user='postgres', password='admin', host='localhost', database='dm3.5')
#     query = 'select * from "public"."Users"'
#     db.send_query(query)
