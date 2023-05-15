from enum import Enum
from typing import List, Optional
# List - нужно импортировать так как предаётся список из ролей
# типом Optional нужно разметить все поля, которые не обязательные, т.к. по умолчанию в pydantic все поля обязательные
from pydantic import BaseModel, StrictStr, Field, StrictBool, ConstrainedDate
# pydantic - для валидации джсонов
from datetime import datetime


class Roles(Enum):
    GUEST = 'Guest'
    PLAYER = 'Player'
    ADMINISTRATOR = 'Administrator'
    NANNY_MODERATOR = 'NannyModerator'
    REGULAR_MODERATOR = 'RegularModerator'
    SENIOR_MODERATOR = 'SeniorModerator'


class Rating(BaseModel):  # нужно создавать отдельный класс, если в джсоне есть 2й уровень вложенности
    enabled: bool
    quality: int
    quantity: int


class User(BaseModel):
    login: StrictStr
    roles: List[Roles]
    medium_picture_url: Optional[StrictStr] = Field(alias='mediumPictureUrl')
    small_picture_url: Optional[StrictStr] = Field(alias='smallPictureUrl')
    status: Optional[StrictStr]
    rating: Rating
    online: Optional[datetime]
    name: Optional[StrictStr]
    location: Optional[StrictStr]
    registration: Optional[datetime]


class UserEnvelopeModel(BaseModel):  # валидация входных моделей от сервера
    resource: User
    metadata: Optional[StrictStr]
