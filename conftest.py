import pytest

from generic.assertions.post_v1_account import AssertionsPostV1Account
from generic.helpers.mailhog import MailhogApi
from generic.helpers.dm_db import DmDatabase
from services.dm_api_account import Facade
import structlog
from vyper import v  # объект который может в себе сохранять переменные окружения и начитывать туда различные
# переменные окружения, а также запускать тесты докере
from pathlib import Path  # для работы с файловой системой, чтобы находить пути

structlog.configure(
    processors=[  # набор процессоров форматируют наш код в консоли. Процессоры лежат в либе structlog
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]  # параметры процессора: indent - отступ в джсоне, ensure_ascii=False - для работы с русской кодировкой
)


@pytest.fixture
def mailhog():  # фикстура
    return MailhogApi(host=v.get('service.mailhog'))  # возвращает клиент


@pytest.fixture
def dm_api_facade(mailhog):  # request вычитывает данные из pytest_addoption
    return Facade(
        host=v.get('service.dm_api_account'),
        mailhog=mailhog
    )  # возвращает клиент


options = (  # для управления параметрами конфига
    'service.dm_api_account',
    'service.mailhog',
    'database.dm3_5.host'
)

connect = None


@pytest.fixture
def dm_db():
    global connect
    if connect is None:  # если есть соединение то мы его не создаём
        connect = DmDatabase(
            user=v.get('database.dm3_5.user'),
            password=v.get('database.dm3_5.password'),
            host=v.get('database.dm3_5.host'),
            database=v.get('database.dm3_5.database')
        )
    yield connect  # если соединения нет , то создаём его
    connect.db.db.close()  # по итогу соединение всегда закрываем


# @pytest.fixture
# def dm_db():
#     db = DmDatabase(
#         user=v.get('database.dm3_5.user'),
#         password=v.get('database.dm3_5.password'),
#         host=v.get('database.dm3_5.host'),
#         database=v.get('database.dm3_5.database')
#     )
#     return db


@pytest.fixture
def assertions(dm_db):
    return AssertionsPostV1Account(dm_db)


@pytest.fixture(autouse=True)  # autouse=True означает что эта опция будет запускаться всегда
def set_config(request):  # request-специальный аргумент который позволяет вычитывать данные
    config = Path(__file__).parent.joinpath('config')  # получаем путь к папке в который лежит конфиг
    config_name = request.config.getoption('--env')  # вытаскиваем название конфига stg.yaml
    v.set_config_name(config_name)  #
    v.add_config_path(config)  # указываем путь к конфигу
    v.read_in_config()  # вычитываем конфиг в наше окружение в питоне
    for option in options:
        v.set(option, request.config.getoption(f'--{option}'))  # установка аргументов и их значений


# хотим указать свой аргумент что нужно запустить  наши тесты на определенном хосте
# используя функцию ниже и аргумент '--env' в конфиг пайтеста дабавляем нужное значение окружения '--env'
def pytest_addoption(parser):
    parser.addoption('--env', action='store', default='stg')  # чтение конфига stg по умолчанию
    for option in options:
        parser.addoption(f'--{option}', action='store', default=None)

# То есть теперь все опции, которые нужны для работы с конфигом , вычитываем в виртуальное окружение и из этого
# виртуального окружения всё запускаем. То есть мы избавилсь от захардкоженных хостов, логинов и паролей и перенесли
# их в файл c конфигурацией stg.yaml
