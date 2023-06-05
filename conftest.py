import pytest
from generic.helpers.mailhog import MailhogApi
from generic.helpers.dm_db import DmDatabase
from services.dm_api_account import Facade
import structlog

structlog.configure(
    processors=[  # набор процессоров форматируют наш код в консоли. Процессоры лежат в либе structlog
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]  # параметры процессора: indent - отступ в джсоне, ensure_ascii=False - для работы с русской кодировкой
)


@pytest.fixture
def mailhog():  # фикстура
    return MailhogApi(host="http://localhost:5025")  # возвращает клиент


@pytest.fixture
def dm_api_facade(mailhog):  # фикстура
    return Facade(host='http://localhost:5051', mailhog=mailhog)  # возвращает клиент


@pytest.fixture
def dm_db():
    db = DmDatabase(user='postgres', password='admin', host='localhost', database='dm3.5')
    return db
