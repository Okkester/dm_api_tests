import requests.exceptions
from requests import session, Response
import structlog
import uuid  # для генерирования ид для event_id
import curlify


class Restclient:
    def __init__(self, host, headers=None):
        self.host = host
        self.session = session()
        if headers:
            self.session.hesders.update(headers)
        self.log = structlog.get_logger(self.__class__.__name__).bind(service='api')  # создание объекта лога. bind -
        # ключ будет отображаться в логировании

    # ниже обертка над нашими рестовыми методами:

    def post(self, path: str, **kwargs) -> Response:
        return self._send_request('POST', path, **kwargs)

    def get(self, path: str, **kwargs) -> Response:
        return self._send_request('GET', path, **kwargs)

    def put(self, path: str, **kwargs) -> Response:   # 26.07 добавил put
        return self._send_request('PUT', path, **kwargs)

    def delete(self, path: str, **kwargs) -> Response:
        return self._send_request('DELETE', path, **kwargs)


    def _send_request(self, method, path, **kwargs):  # 23.27 - в уроке объяснение что происходит
        full_url = self.host + path
        log = self.log.bind(
            event_id=str(uuid.uuid4()))  # для каждого события с отправкой запроса будем создавать какой-то ивент
        log.msg(  # формирование лога с теми данными, которые нам нужны
            event='request',
            method=method,
            full_url=full_url,
            params=kwargs.get('params'),  # params читается из **kwargs с помощью метода get
            headers=kwargs.get('headers'),
            json=kwargs.get('json'),
            data=kwargs.get('data')
        )
        response = self.session.request(  # в эту будет сохраняться результат запроса
            method=method,
            url=full_url,
            **kwargs
        )
        curl = curlify.to_curl(response.request)  # формирование курла для дебага разрабу
        print(curl)
        log.msg(
            event='response',
            status_code=response.status_code,
            headers=response.headers,
            json=self._get_json(response),
            content=response.content,
            curl=curl
        )
        return response

    @staticmethod  # метод статический так как не используем функции и тд из класса Restclient
    def _get_json(response):  # ф-я к-я помогает избежать ошибки преобразования объекта в джсон
        try:
            return response.json()
        except requests.exceptions.JSONDecodeError:  # путь до исключенияв в ошибке
            return
