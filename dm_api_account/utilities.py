import allure
import requests
from pydantic import BaseModel


def validate_request_json(json: dict | BaseModel):
    # для валидации json на входе и возможности отключения валидации для проведения негативных проверок
    if isinstance(json, dict):  # isinstance проверяет в модели джсон или нет
        return json
    return json.dict(by_alias=True, exclude_none=True)  # преобразование джсон в dict


def validate_status_code(response: requests.Response, status_code: int):
    with allure.step("Проверка валидации и статус кода"):
        assert response.status_code == status_code, \
            f'Статус-код ответа должен быть равен {status_code},но он равен {response.status_code}'
