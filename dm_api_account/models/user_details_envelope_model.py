from enum import Enum
from typing import List, Optional
# List - нужно импортировать так как предаётся список из ролей
# типом Optional нужно разметить все поля, которые не обязательные, т.к. по умолчанию в pydantic все поля обязательные
from pydantic import BaseModel, StrictStr, Field, StrictBool, ConstrainedDate
# pydantic - для валидации джсонов


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


class Info(BaseModel):
    value: Optional[StrictStr]
    parseMode: Optional[StrictStr]


class Paging:
    postsPerPage: int
    commentsPerPage: int
    topicsPerPage: int
    messagesPerPage: int
    entitiesPerPage: int


class Settings(BaseModel):
    colorSchema: Optional[StrictStr]
    nannyGreetingsMessage: Optional[StrictStr]
    paging: Paging


class UserDetails(BaseModel):
    login: StrictStr
    roles: List[Roles]
    medium_picture_url: Optional[StrictStr] = Field(alias='mediumPictureUrl')
    small_picture_url: Optional[StrictStr] = Field(alias='smallPictureUrl')
    status: Optional[StrictStr]
    rating: Rating
    online: Optional[ConstrainedDate]
    name: Optional[StrictStr]
    location: Optional[StrictStr]
    registration: Optional[ConstrainedDate]
    icq: Optional[ConstrainedDate]
    skype: Optional[ConstrainedDate]
    originalPictureUrl: Optional[ConstrainedDate]
    info: Info
    settings: Settings


class UserDetailsEnvelopeModel(BaseModel):  # валидация входных моделей от сервера
    resource: UserDetails
    metadata: Optional[StrictStr]
