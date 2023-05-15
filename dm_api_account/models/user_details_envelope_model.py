from enum import Enum
from typing import List, Optional
# List - нужно импортировать так как передаётся список из ролей
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


class Info(BaseModel):
    value: Optional[StrictStr]
    parse_mode: Optional[StrictStr] = Field(alias='parseMode')


class Paging:
    posts_per_page: int = Field(alias='postsPerPage')
    comments_per_page: int = Field(alias='commentsPerPage')
    topics_per_page: int = Field(alias='topicsPerPage')
    messages_per_page: int = Field(alias='messagesPerPage')
    entities_per_page: int = Field(alias='entitiesPerPage')


class Settings(BaseModel):
    color_schema: Optional[StrictStr] = Field(alias='colorSchema')
    nanny_greetings_message: Optional[StrictStr] = Field(alias='nannyGreetingsMessage')
    paging: Paging


class UserDetails(BaseModel):
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
    icq: Optional[StrictStr]
    skype: Optional[StrictStr]
    original_picture_url: Optional[StrictStr] = Field(alias='originalPictureUrl')
    info: Info
    settings: Settings


class UserDetailsEnvelopeModel(BaseModel):  # валидация входных моделей от сервера
    resource: UserDetails
    metadata: Optional[StrictStr]
