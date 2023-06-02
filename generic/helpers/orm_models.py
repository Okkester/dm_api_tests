# from sqlalchemy import create_engine, text, \
#     Column, String, Boolean, select  # для создания подключения к базе. text - для написания запроса в виде текста
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.dialects.postgresql import UUID
#
#
# Base = declarative_base()
#
#
# class User(Base):  # описываем модель таблицы Users
#     __tablename__ = 'Users'
#
#     UserId = Column(UUID, primary_key=True)  # primary_key - ключевое поле
#     Login = Column(String(100))  # 100 - количество символов в поле
#     Email = Column(String(100))
#     Name = Column(String(100))
#     Activated = Column(Boolean, nullable=False)  # nullable=False - чтобы поле Activated не могло быть равно null

from sqlalchemy import Boolean, Column, DateTime, Float, ForeignKeyConstraint, Index, Integer, PrimaryKeyConstraint, SmallInteger, String, Text, text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Conversations(Base):
    __tablename__ = 'Conversations'
    __table_args__ = (
        ForeignKeyConstraint(['LastMessageId'], ['Messages.MessageId'], ondelete='RESTRICT', name='FK_Conversations_Messages_LastMessageId'),
        PrimaryKeyConstraint('ConversationId', name='PK_Conversations'),
        Index('IX_Conversations_LastMessageId', 'LastMessageId')
    )

    ConversationId = Column(UUID)
    Visavi = Column(Boolean, nullable=False, server_default=text('false'))
    LastMessageId = Column(UUID)

    Messages = relationship('Messages', foreign_keys=[LastMessageId], back_populates='Conversations_')
    Messages_ = relationship('Messages', foreign_keys='[Messages.ConversationId]', back_populates='Conversations1')
    UserConversationLinks = relationship('UserConversationLinks', back_populates='Conversations_')


class Fora(Base):
    __tablename__ = 'Fora'
    __table_args__ = (
        PrimaryKeyConstraint('ForumId', name='PK_Fora'),
    )

    ForumId = Column(UUID)
    Order = Column(Integer, nullable=False)
    ViewPolicy = Column(Integer, nullable=False)
    CreateTopicPolicy = Column(Integer, nullable=False)
    Title = Column(Text)
    Description = Column(Text)

    ForumModerators = relationship('ForumModerators', back_populates='Fora_')
    ForumTopics = relationship('ForumTopics', back_populates='Fora_')


class Messages(Base):
    __tablename__ = 'Messages'
    __table_args__ = (
        ForeignKeyConstraint(['ConversationId'], ['Conversations.ConversationId'], ondelete='CASCADE', name='FK_Messages_Conversations_ConversationId'),
        ForeignKeyConstraint(['UserId'], ['Users.UserId'], ondelete='CASCADE', name='FK_Messages_Users_UserId'),
        PrimaryKeyConstraint('MessageId', name='PK_Messages'),
        Index('IX_Messages_ConversationId', 'ConversationId'),
        Index('IX_Messages_UserId', 'UserId')
    )

    MessageId = Column(UUID)
    UserId = Column(UUID, nullable=False)
    ConversationId = Column(UUID, nullable=False)
    CreateDate = Column(DateTime(True), nullable=False)
    IsRemoved = Column(Boolean, nullable=False)
    Text_ = Column('Text', Text)

    Conversations_ = relationship('Conversations', foreign_keys='[Conversations.LastMessageId]', back_populates='Messages')
    Conversations1 = relationship('Conversations', foreign_keys=[ConversationId], back_populates='Messages_')
    Users = relationship('Users', back_populates='Messages_')


class TagGroups(Base):
    __tablename__ = 'TagGroups'
    __table_args__ = (
        PrimaryKeyConstraint('TagGroupId', name='PK_TagGroups'),
    )

    TagGroupId = Column(UUID)
    Title = Column(Text)

    Tags = relationship('Tags', back_populates='TagGroups_')


class Users(Base):
    __tablename__ = 'Users'
    __table_args__ = (
        PrimaryKeyConstraint('UserId', name='PK_Users'),
    )

    UserId = Column(UUID)
    RegistrationDate = Column(DateTime(True), nullable=False)
    Role = Column(Integer, nullable=False)
    AccessPolicy = Column(Integer, nullable=False)
    RatingDisabled = Column(Boolean, nullable=False)
    QualityRating = Column(Integer, nullable=False)
    QuantityRating = Column(Integer, nullable=False)
    Activated = Column(Boolean, nullable=False)
    CanMerge = Column(Boolean, nullable=False)
    IsRemoved = Column(Boolean, nullable=False)
    Login = Column(String(100))
    Email = Column(String(100))
    LastVisitDate = Column(DateTime(True))
    TimezoneId = Column(Text)
    Salt = Column(String(120))
    PasswordHash = Column(String(300))
    MergeRequested = Column(UUID)
    Status = Column(String(200))
    Name = Column(String(100))
    Location = Column(String(100))
    Icq = Column(String(20))
    Skype = Column(String(50))
    Info = Column(Text)
    ProfilePictureUrl = Column(String(200))
    MediumProfilePictureUrl = Column(String(200))
    SmallProfilePictureUrl = Column(String(200))

    Messages_ = relationship('Messages', back_populates='Users')
    Bans = relationship('Bans', foreign_keys='[Bans.ModeratorId]', back_populates='Users_')
    Bans_ = relationship('Bans', foreign_keys='[Bans.UserId]', back_populates='Users1')
    ChatMessages = relationship('ChatMessages', back_populates='Users_')
    Comments = relationship('Comments', back_populates='Users_')
    ForumModerators = relationship('ForumModerators', back_populates='Users_')
    Games = relationship('Games', foreign_keys='[Games.AssistantId]', back_populates='Users_')
    Games_ = relationship('Games', foreign_keys='[Games.MasterId]', back_populates='Users1')
    Games1 = relationship('Games', foreign_keys='[Games.NannyId]', back_populates='Users2')
    Likes = relationship('Likes', back_populates='Users_')
    Reports = relationship('Reports', foreign_keys='[Reports.AnswerAuthorId]', back_populates='Users_')
    Reports_ = relationship('Reports', foreign_keys='[Reports.TargetId]', back_populates='Users1')
    Reports1 = relationship('Reports', foreign_keys='[Reports.UserId]', back_populates='Users2')
    Reviews = relationship('Reviews', back_populates='Users_')
    Tokens = relationship('Tokens', back_populates='Users_')
    Uploads = relationship('Uploads', back_populates='Users_')
    UserConversationLinks = relationship('UserConversationLinks', back_populates='Users_')
    Warnings = relationship('Warnings', foreign_keys='[Warnings.ModeratorId]', back_populates='Users_')
    Warnings_ = relationship('Warnings', foreign_keys='[Warnings.UserId]', back_populates='Users1')
    BlackListLinks = relationship('BlackListLinks', back_populates='Users_')
    Characters = relationship('Characters', back_populates='Users_')
    ForumTopics = relationship('ForumTopics', back_populates='Users_')
    Readers = relationship('Readers', back_populates='Users_')
    PendingPosts = relationship('PendingPosts', foreign_keys='[PendingPosts.AwaitingUserId]', back_populates='Users_')
    PendingPosts_ = relationship('PendingPosts', foreign_keys='[PendingPosts.PendingUserId]', back_populates='Users1')
    Posts = relationship('Posts', foreign_keys='[Posts.LastUpdateUserId]', back_populates='Users_')
    Posts_ = relationship('Posts', foreign_keys='[Posts.UserId]', back_populates='Users1')
    Votes = relationship('Votes', foreign_keys='[Votes.TargetUserId]', back_populates='Users_')
    Votes_ = relationship('Votes', foreign_keys='[Votes.UserId]', back_populates='Users1')


class EFMigrationsHistory(Base):
    __tablename__ = '__EFMigrationsHistory'
    __table_args__ = (
        PrimaryKeyConstraint('MigrationId', name='PK___EFMigrationsHistory'),
    )

    MigrationId = Column(String(150))
    ProductVersion = Column(String(32), nullable=False)


class Bans(Base):
    __tablename__ = 'Bans'
    __table_args__ = (
        ForeignKeyConstraint(['ModeratorId'], ['Users.UserId'], ondelete='CASCADE', name='FK_Bans_Users_ModeratorId'),
        ForeignKeyConstraint(['UserId'], ['Users.UserId'], ondelete='CASCADE', name='FK_Bans_Users_UserId'),
        PrimaryKeyConstraint('BanId', name='PK_Bans'),
        Index('IX_Bans_ModeratorId', 'ModeratorId'),
        Index('IX_Bans_UserId', 'UserId')
    )

    BanId = Column(UUID)
    UserId = Column(UUID, nullable=False)
    ModeratorId = Column(UUID, nullable=False)
    StartDate = Column(DateTime(True), nullable=False)
    EndDate = Column(DateTime(True), nullable=False)
    AccessRestrictionPolicy = Column(Integer, nullable=False)
    IsVoluntary = Column(Boolean, nullable=False)
    IsRemoved = Column(Boolean, nullable=False)
    Comment = Column(Text)

    Users_ = relationship('Users', foreign_keys=[ModeratorId], back_populates='Bans')
    Users1 = relationship('Users', foreign_keys=[UserId], back_populates='Bans_')


class ChatMessages(Base):
    __tablename__ = 'ChatMessages'
    __table_args__ = (
        ForeignKeyConstraint(['UserId'], ['Users.UserId'], ondelete='CASCADE', name='FK_ChatMessages_Users_UserId'),
        PrimaryKeyConstraint('ChatMessageId', name='PK_ChatMessages'),
        Index('IX_ChatMessages_UserId', 'UserId')
    )

    ChatMessageId = Column(UUID)
    UserId = Column(UUID, nullable=False)
    CreateDate = Column(DateTime(True), nullable=False)
    Text_ = Column('Text', Text)

    Users_ = relationship('Users', back_populates='ChatMessages')


class Comments(Base):
    __tablename__ = 'Comments'
    __table_args__ = (
        ForeignKeyConstraint(['UserId'], ['Users.UserId'], ondelete='CASCADE', name='FK_Comments_Users_UserId'),
        PrimaryKeyConstraint('CommentId', name='PK_Comments'),
        Index('IX_Comments_EntityId', 'EntityId'),
        Index('IX_Comments_UserId', 'UserId')
    )

    CommentId = Column(UUID)
    EntityId = Column(UUID, nullable=False)
    UserId = Column(UUID, nullable=False)
    CreateDate = Column(DateTime(True), nullable=False)
    IsRemoved = Column(Boolean, nullable=False)
    LastUpdateDate = Column(DateTime(True))
    Text_ = Column('Text', Text)

    Users_ = relationship('Users', back_populates='Comments')
    ForumTopics = relationship('ForumTopics', back_populates='Comments_')


class ForumModerators(Base):
    __tablename__ = 'ForumModerators'
    __table_args__ = (
        ForeignKeyConstraint(['ForumId'], ['Fora.ForumId'], ondelete='CASCADE', name='FK_ForumModerators_Fora_ForumId'),
        ForeignKeyConstraint(['UserId'], ['Users.UserId'], ondelete='CASCADE', name='FK_ForumModerators_Users_UserId'),
        PrimaryKeyConstraint('ForumModeratorId', name='PK_ForumModerators'),
        Index('IX_ForumModerators_ForumId', 'ForumId'),
        Index('IX_ForumModerators_UserId', 'UserId')
    )

    ForumModeratorId = Column(UUID)
    ForumId = Column(UUID, nullable=False)
    UserId = Column(UUID, nullable=False)

    Fora_ = relationship('Fora', back_populates='ForumModerators')
    Users_ = relationship('Users', back_populates='ForumModerators')


class Games(Base):
    __tablename__ = 'Games'
    __table_args__ = (
        ForeignKeyConstraint(['AssistantId'], ['Users.UserId'], ondelete='RESTRICT', name='FK_Games_Users_AssistantId'),
        ForeignKeyConstraint(['MasterId'], ['Users.UserId'], ondelete='CASCADE', name='FK_Games_Users_MasterId'),
        ForeignKeyConstraint(['NannyId'], ['Users.UserId'], ondelete='RESTRICT', name='FK_Games_Users_NannyId'),
        PrimaryKeyConstraint('GameId', name='PK_Games'),
        Index('IX_Games_AssistantId', 'AssistantId'),
        Index('IX_Games_MasterId', 'MasterId'),
        Index('IX_Games_NannyId', 'NannyId')
    )

    GameId = Column(UUID)
    CreateDate = Column(DateTime(True), nullable=False)
    Status = Column(Integer, nullable=False)
    MasterId = Column(UUID, nullable=False)
    HideTemper = Column(Boolean, nullable=False)
    HideSkills = Column(Boolean, nullable=False)
    HideInventory = Column(Boolean, nullable=False)
    HideStory = Column(Boolean, nullable=False)
    DisableAlignment = Column(Boolean, nullable=False)
    HideDiceResult = Column(Boolean, nullable=False)
    ShowPrivateMessages = Column(Boolean, nullable=False)
    CommentariesAccessMode = Column(Integer, nullable=False)
    IsRemoved = Column(Boolean, nullable=False)
    ReleaseDate = Column(DateTime(True))
    AssistantId = Column(UUID)
    NannyId = Column(UUID)
    AttributeSchemaId = Column(UUID)
    Title = Column(Text)
    SystemName = Column(Text)
    SettingName = Column(Text)
    Info = Column(Text)
    Notepad = Column(Text)

    Users_ = relationship('Users', foreign_keys=[AssistantId], back_populates='Games')
    Users1 = relationship('Users', foreign_keys=[MasterId], back_populates='Games_')
    Users2 = relationship('Users', foreign_keys=[NannyId], back_populates='Games1')
    BlackListLinks = relationship('BlackListLinks', back_populates='Games_')
    Characters = relationship('Characters', back_populates='Games_')
    GameTags = relationship('GameTags', back_populates='Games_')
    Readers = relationship('Readers', back_populates='Games_')
    Rooms = relationship('Rooms', back_populates='Games_')
    Votes = relationship('Votes', back_populates='Games_')


class Likes(Base):
    __tablename__ = 'Likes'
    __table_args__ = (
        ForeignKeyConstraint(['UserId'], ['Users.UserId'], ondelete='CASCADE', name='FK_Likes_Users_UserId'),
        PrimaryKeyConstraint('LikeId', name='PK_Likes'),
        Index('IX_Likes_EntityId', 'EntityId'),
        Index('IX_Likes_UserId', 'UserId')
    )

    LikeId = Column(UUID)
    EntityId = Column(UUID, nullable=False)
    UserId = Column(UUID, nullable=False)

    Users_ = relationship('Users', back_populates='Likes')


class Reports(Base):
    __tablename__ = 'Reports'
    __table_args__ = (
        ForeignKeyConstraint(['AnswerAuthorId'], ['Users.UserId'], ondelete='RESTRICT', name='FK_Reports_Users_AnswerAuthorId'),
        ForeignKeyConstraint(['TargetId'], ['Users.UserId'], ondelete='CASCADE', name='FK_Reports_Users_TargetId'),
        ForeignKeyConstraint(['UserId'], ['Users.UserId'], ondelete='CASCADE', name='FK_Reports_Users_UserId'),
        PrimaryKeyConstraint('ReportId', name='PK_Reports'),
        Index('IX_Reports_AnswerAuthorId', 'AnswerAuthorId'),
        Index('IX_Reports_TargetId', 'TargetId'),
        Index('IX_Reports_UserId', 'UserId')
    )

    ReportId = Column(UUID)
    UserId = Column(UUID, nullable=False)
    TargetId = Column(UUID, nullable=False)
    CreateDate = Column(DateTime(True), nullable=False)
    ReportText = Column(Text)
    Comment = Column(Text)
    AnswerAuthorId = Column(UUID)
    Answer = Column(Text)

    Users_ = relationship('Users', foreign_keys=[AnswerAuthorId], back_populates='Reports')
    Users1 = relationship('Users', foreign_keys=[TargetId], back_populates='Reports_')
    Users2 = relationship('Users', foreign_keys=[UserId], back_populates='Reports1')


class Reviews(Base):
    __tablename__ = 'Reviews'
    __table_args__ = (
        ForeignKeyConstraint(['UserId'], ['Users.UserId'], ondelete='CASCADE', name='FK_Reviews_Users_UserId'),
        PrimaryKeyConstraint('ReviewId', name='PK_Reviews'),
        Index('IX_Reviews_UserId', 'UserId')
    )

    ReviewId = Column(UUID)
    UserId = Column(UUID, nullable=False)
    CreateDate = Column(DateTime(True), nullable=False)
    IsApproved = Column(Boolean, nullable=False)
    IsRemoved = Column(Boolean, nullable=False, server_default=text('false'))
    Text_ = Column('Text', Text)

    Users_ = relationship('Users', back_populates='Reviews')


class Tags(Base):
    __tablename__ = 'Tags'
    __table_args__ = (
        ForeignKeyConstraint(['TagGroupId'], ['TagGroups.TagGroupId'], ondelete='CASCADE', name='FK_Tags_TagGroups_TagGroupId'),
        PrimaryKeyConstraint('TagId', name='PK_Tags'),
        Index('IX_Tags_TagGroupId', 'TagGroupId')
    )

    TagId = Column(UUID)
    TagGroupId = Column(UUID, nullable=False)
    Title = Column(Text)

    TagGroups_ = relationship('TagGroups', back_populates='Tags')
    GameTags = relationship('GameTags', back_populates='Tags_')


class Tokens(Base):
    __tablename__ = 'Tokens'
    __table_args__ = (
        ForeignKeyConstraint(['UserId'], ['Users.UserId'], ondelete='CASCADE', name='FK_Tokens_Users_UserId'),
        PrimaryKeyConstraint('TokenId', name='PK_Tokens'),
        Index('IX_Tokens_EntityId', 'EntityId'),
        Index('IX_Tokens_UserId', 'UserId')
    )

    TokenId = Column(UUID)
    UserId = Column(UUID, nullable=False)
    CreateDate = Column(DateTime(True), nullable=False)
    Type = Column(Integer, nullable=False)
    IsRemoved = Column(Boolean, nullable=False)
    EntityId = Column(UUID)

    Users_ = relationship('Users', back_populates='Tokens')


class Uploads(Base):
    __tablename__ = 'Uploads'
    __table_args__ = (
        ForeignKeyConstraint(['UserId'], ['Users.UserId'], ondelete='CASCADE', name='FK_Uploads_Users_UserId'),
        PrimaryKeyConstraint('UploadId', name='PK_Uploads'),
        Index('IX_Uploads_EntityId', 'EntityId'),
        Index('IX_Uploads_UserId', 'UserId')
    )

    UploadId = Column(UUID)
    CreateDate = Column(DateTime(True), nullable=False)
    UserId = Column(UUID, nullable=False)
    IsRemoved = Column(Boolean, nullable=False)
    Original = Column(Boolean, nullable=False, server_default=text('false'))
    EntityId = Column(UUID)
    FilePath = Column(Text)
    FileName = Column(Text)

    Users_ = relationship('Users', back_populates='Uploads')


class UserConversationLinks(Base):
    __tablename__ = 'UserConversationLinks'
    __table_args__ = (
        ForeignKeyConstraint(['ConversationId'], ['Conversations.ConversationId'], ondelete='CASCADE', name='FK_UserConversationLinks_Conversations_ConversationId'),
        ForeignKeyConstraint(['UserId'], ['Users.UserId'], ondelete='CASCADE', name='FK_UserConversationLinks_Users_UserId'),
        PrimaryKeyConstraint('UserConversationLinkId', name='PK_UserConversationLinks'),
        Index('IX_UserConversationLinks_ConversationId', 'ConversationId'),
        Index('IX_UserConversationLinks_UserId', 'UserId')
    )

    UserConversationLinkId = Column(UUID)
    UserId = Column(UUID, nullable=False)
    ConversationId = Column(UUID, nullable=False)
    IsRemoved = Column(Boolean, nullable=False)

    Conversations_ = relationship('Conversations', back_populates='UserConversationLinks')
    Users_ = relationship('Users', back_populates='UserConversationLinks')


class Warnings(Base):
    __tablename__ = 'Warnings'
    __table_args__ = (
        ForeignKeyConstraint(['ModeratorId'], ['Users.UserId'], ondelete='CASCADE', name='FK_Warnings_Users_ModeratorId'),
        ForeignKeyConstraint(['UserId'], ['Users.UserId'], ondelete='CASCADE', name='FK_Warnings_Users_UserId'),
        PrimaryKeyConstraint('WarningId', name='PK_Warnings'),
        Index('IX_Warnings_EntityId', 'EntityId'),
        Index('IX_Warnings_ModeratorId', 'ModeratorId'),
        Index('IX_Warnings_UserId', 'UserId')
    )

    WarningId = Column(UUID)
    UserId = Column(UUID, nullable=False)
    ModeratorId = Column(UUID, nullable=False)
    EntityId = Column(UUID, nullable=False)
    CreateDate = Column(DateTime(True), nullable=False)
    Points = Column(Integer, nullable=False)
    IsRemoved = Column(Boolean, nullable=False)
    Text_ = Column('Text', Text)

    Users_ = relationship('Users', foreign_keys=[ModeratorId], back_populates='Warnings')
    Users1 = relationship('Users', foreign_keys=[UserId], back_populates='Warnings_')


class BlackListLinks(Base):
    __tablename__ = 'BlackListLinks'
    __table_args__ = (
        ForeignKeyConstraint(['GameId'], ['Games.GameId'], ondelete='CASCADE', name='FK_BlackListLinks_Games_GameId'),
        ForeignKeyConstraint(['UserId'], ['Users.UserId'], ondelete='CASCADE', name='FK_BlackListLinks_Users_UserId'),
        PrimaryKeyConstraint('BlackListLinkId', name='PK_BlackListLinks'),
        Index('IX_BlackListLinks_GameId', 'GameId'),
        Index('IX_BlackListLinks_UserId', 'UserId')
    )

    BlackListLinkId = Column(UUID)
    GameId = Column(UUID, nullable=False)
    UserId = Column(UUID, nullable=False)

    Games_ = relationship('Games', back_populates='BlackListLinks')
    Users_ = relationship('Users', back_populates='BlackListLinks')


class Characters(Base):
    __tablename__ = 'Characters'
    __table_args__ = (
        ForeignKeyConstraint(['GameId'], ['Games.GameId'], ondelete='CASCADE', name='FK_Characters_Games_GameId'),
        ForeignKeyConstraint(['UserId'], ['Users.UserId'], ondelete='CASCADE', name='FK_Characters_Users_UserId'),
        PrimaryKeyConstraint('CharacterId', name='PK_Characters'),
        Index('IX_Characters_GameId', 'GameId'),
        Index('IX_Characters_UserId', 'UserId')
    )

    CharacterId = Column(UUID)
    GameId = Column(UUID, nullable=False)
    UserId = Column(UUID, nullable=False)
    Status = Column(Integer, nullable=False)
    CreateDate = Column(DateTime(True), nullable=False)
    IsNpc = Column(Boolean, nullable=False)
    AccessPolicy = Column(Integer, nullable=False)
    IsRemoved = Column(Boolean, nullable=False)
    LastUpdateDate = Column(DateTime(True))
    Name = Column(Text)
    Race = Column(Text)
    Class = Column(Text)
    Alignment = Column(Integer)
    Appearance = Column(Text)
    Temper = Column(Text)
    Story = Column(Text)
    Skills = Column(Text)
    Inventory = Column(Text)

    Games_ = relationship('Games', back_populates='Characters')
    Users_ = relationship('Users', back_populates='Characters')
    CharacterAttributes = relationship('CharacterAttributes', back_populates='Characters_')
    Posts = relationship('Posts', back_populates='Characters_')
    RoomClaims = relationship('RoomClaims', back_populates='Characters_')


class ForumTopics(Base):
    __tablename__ = 'ForumTopics'
    __table_args__ = (
        ForeignKeyConstraint(['ForumId'], ['Fora.ForumId'], ondelete='CASCADE', name='FK_ForumTopics_Fora_ForumId'),
        ForeignKeyConstraint(['LastCommentId'], ['Comments.CommentId'], ondelete='RESTRICT', name='FK_ForumTopics_Comments_LastCommentId'),
        ForeignKeyConstraint(['UserId'], ['Users.UserId'], ondelete='CASCADE', name='FK_ForumTopics_Users_UserId'),
        PrimaryKeyConstraint('ForumTopicId', name='PK_ForumTopics'),
        Index('IX_ForumTopics_ForumId', 'ForumId'),
        Index('IX_ForumTopics_LastCommentId', 'LastCommentId'),
        Index('IX_ForumTopics_UserId', 'UserId')
    )

    ForumTopicId = Column(UUID)
    ForumId = Column(UUID, nullable=False)
    UserId = Column(UUID, nullable=False)
    CreateDate = Column(DateTime(True), nullable=False)
    Attached = Column(Boolean, nullable=False)
    Closed = Column(Boolean, nullable=False)
    IsRemoved = Column(Boolean, nullable=False)
    Title = Column(Text)
    Text_ = Column('Text', Text)
    LastCommentId = Column(UUID)

    Fora_ = relationship('Fora', back_populates='ForumTopics')
    Comments_ = relationship('Comments', back_populates='ForumTopics')
    Users_ = relationship('Users', back_populates='ForumTopics')


class GameTags(Base):
    __tablename__ = 'GameTags'
    __table_args__ = (
        ForeignKeyConstraint(['GameId'], ['Games.GameId'], ondelete='CASCADE', name='FK_GameTags_Games_GameId'),
        ForeignKeyConstraint(['TagId'], ['Tags.TagId'], ondelete='CASCADE', name='FK_GameTags_Tags_TagId'),
        PrimaryKeyConstraint('GameTagId', name='PK_GameTags'),
        Index('IX_GameTags_GameId', 'GameId'),
        Index('IX_GameTags_TagId', 'TagId')
    )

    GameTagId = Column(UUID)
    GameId = Column(UUID, nullable=False)
    TagId = Column(UUID, nullable=False)

    Games_ = relationship('Games', back_populates='GameTags')
    Tags_ = relationship('Tags', back_populates='GameTags')


class Readers(Base):
    __tablename__ = 'Readers'
    __table_args__ = (
        ForeignKeyConstraint(['GameId'], ['Games.GameId'], ondelete='CASCADE', name='FK_Readers_Games_GameId'),
        ForeignKeyConstraint(['UserId'], ['Users.UserId'], ondelete='CASCADE', name='FK_Readers_Users_UserId'),
        PrimaryKeyConstraint('ReaderId', name='PK_Readers'),
        Index('IX_Readers_GameId', 'GameId'),
        Index('IX_Readers_UserId', 'UserId')
    )

    ReaderId = Column(UUID)
    GameId = Column(UUID, nullable=False)
    UserId = Column(UUID, nullable=False)

    Games_ = relationship('Games', back_populates='Readers')
    Users_ = relationship('Users', back_populates='Readers')
    RoomClaims = relationship('RoomClaims', back_populates='Readers_')


class Rooms(Base):
    __tablename__ = 'Rooms'
    __table_args__ = (
        ForeignKeyConstraint(['GameId'], ['Games.GameId'], ondelete='CASCADE', name='FK_Rooms_Games_GameId'),
        ForeignKeyConstraint(['NextRoomId'], ['Rooms.RoomId'], ondelete='RESTRICT', name='FK_Rooms_Rooms_NextRoomId'),
        ForeignKeyConstraint(['PreviousRoomId'], ['Rooms.RoomId'], ondelete='RESTRICT', name='FK_Rooms_Rooms_PreviousRoomId'),
        PrimaryKeyConstraint('RoomId', name='PK_Rooms'),
        Index('IX_Rooms_GameId', 'GameId'),
        Index('IX_Rooms_NextRoomId', 'NextRoomId', unique=True),
        Index('IX_Rooms_PreviousRoomId', 'PreviousRoomId')
    )

    RoomId = Column(UUID)
    GameId = Column(UUID, nullable=False)
    AccessType = Column(Integer, nullable=False)
    Type = Column(Integer, nullable=False)
    OrderNumber = Column(Float(53), nullable=False)
    IsRemoved = Column(Boolean, nullable=False)
    Title = Column(Text)
    PreviousRoomId = Column(UUID)
    NextRoomId = Column(UUID)

    Games_ = relationship('Games', back_populates='Rooms')
    Rooms = relationship('Rooms', remote_side=[RoomId], foreign_keys=[NextRoomId], back_populates='Rooms_reverse')
    Rooms_reverse = relationship('Rooms', remote_side=[NextRoomId], foreign_keys=[NextRoomId], back_populates='Rooms')
    Rooms_ = relationship('Rooms', remote_side=[RoomId], foreign_keys=[PreviousRoomId], back_populates='Rooms__reverse')
    Rooms__reverse = relationship('Rooms', remote_side=[PreviousRoomId], foreign_keys=[PreviousRoomId], back_populates='Rooms_')
    PendingPosts = relationship('PendingPosts', back_populates='Rooms_')
    Posts = relationship('Posts', back_populates='Rooms_')
    RoomClaims = relationship('RoomClaims', back_populates='Rooms_')


class CharacterAttributes(Base):
    __tablename__ = 'CharacterAttributes'
    __table_args__ = (
        ForeignKeyConstraint(['CharacterId'], ['Characters.CharacterId'], ondelete='CASCADE', name='FK_CharacterAttributes_Characters_CharacterId'),
        PrimaryKeyConstraint('CharacterAttributeId', name='PK_CharacterAttributes'),
        Index('IX_CharacterAttributes_CharacterId', 'CharacterId')
    )

    CharacterAttributeId = Column(UUID)
    AttributeId = Column(UUID, nullable=False)
    CharacterId = Column(UUID, nullable=False)
    Value = Column(Text)

    Characters_ = relationship('Characters', back_populates='CharacterAttributes')


class PendingPosts(Base):
    __tablename__ = 'PendingPosts'
    __table_args__ = (
        ForeignKeyConstraint(['AwaitingUserId'], ['Users.UserId'], ondelete='CASCADE', name='FK_PendingPosts_Users_AwaitingUserId'),
        ForeignKeyConstraint(['PendingUserId'], ['Users.UserId'], ondelete='CASCADE', name='FK_PendingPosts_Users_PendingUserId'),
        ForeignKeyConstraint(['RoomId'], ['Rooms.RoomId'], ondelete='CASCADE', name='FK_PendingPosts_Rooms_RoomId'),
        PrimaryKeyConstraint('PendingPostId', name='PK_PendingPosts'),
        Index('IX_PendingPosts_AwaitingUserId', 'AwaitingUserId'),
        Index('IX_PendingPosts_PendingUserId', 'PendingUserId'),
        Index('IX_PendingPosts_RoomId', 'RoomId')
    )

    PendingPostId = Column(UUID)
    AwaitingUserId = Column(UUID, nullable=False)
    PendingUserId = Column(UUID, nullable=False)
    RoomId = Column(UUID, nullable=False)
    CreateDate = Column(DateTime(True), nullable=False)

    Users_ = relationship('Users', foreign_keys=[AwaitingUserId], back_populates='PendingPosts')
    Users1 = relationship('Users', foreign_keys=[PendingUserId], back_populates='PendingPosts_')
    Rooms_ = relationship('Rooms', back_populates='PendingPosts')


class Posts(Base):
    __tablename__ = 'Posts'
    __table_args__ = (
        ForeignKeyConstraint(['CharacterId'], ['Characters.CharacterId'], ondelete='RESTRICT', name='FK_Posts_Characters_CharacterId'),
        ForeignKeyConstraint(['LastUpdateUserId'], ['Users.UserId'], ondelete='RESTRICT', name='FK_Posts_Users_LastUpdateUserId'),
        ForeignKeyConstraint(['RoomId'], ['Rooms.RoomId'], ondelete='CASCADE', name='FK_Posts_Rooms_RoomId'),
        ForeignKeyConstraint(['UserId'], ['Users.UserId'], ondelete='CASCADE', name='FK_Posts_Users_UserId'),
        PrimaryKeyConstraint('PostId', name='PK_Posts'),
        Index('IX_Posts_CharacterId', 'CharacterId'),
        Index('IX_Posts_LastUpdateUserId', 'LastUpdateUserId'),
        Index('IX_Posts_RoomId', 'RoomId'),
        Index('IX_Posts_UserId', 'UserId')
    )

    PostId = Column(UUID)
    RoomId = Column(UUID, nullable=False)
    UserId = Column(UUID, nullable=False)
    CreateDate = Column(DateTime(True), nullable=False)
    IsRemoved = Column(Boolean, nullable=False)
    CharacterId = Column(UUID)
    LastUpdateUserId = Column(UUID)
    LastUpdateDate = Column(DateTime(True))
    Text_ = Column('Text', Text)
    Commentary = Column(Text)
    MasterMessage = Column(Text)

    Characters_ = relationship('Characters', back_populates='Posts')
    Users_ = relationship('Users', foreign_keys=[LastUpdateUserId], back_populates='Posts')
    Rooms_ = relationship('Rooms', back_populates='Posts')
    Users1 = relationship('Users', foreign_keys=[UserId], back_populates='Posts_')
    Votes = relationship('Votes', back_populates='Posts_')


class RoomClaims(Base):
    __tablename__ = 'RoomClaims'
    __table_args__ = (
        ForeignKeyConstraint(['ParticipantId'], ['Readers.ReaderId'], ondelete='CASCADE', name='FK_RoomClaims_Readers_ParticipantId'),
        ForeignKeyConstraint(['ParticipantId'], ['Characters.CharacterId'], ondelete='CASCADE', name='FK_RoomClaims_Characters_ParticipantId'),
        ForeignKeyConstraint(['RoomId'], ['Rooms.RoomId'], ondelete='CASCADE', name='FK_RoomClaims_Rooms_RoomId'),
        PrimaryKeyConstraint('RoomClaimId', name='PK_RoomClaims'),
        Index('IX_RoomClaims_ParticipantId', 'ParticipantId'),
        Index('IX_RoomClaims_RoomId', 'RoomId')
    )

    RoomClaimId = Column(UUID)
    ParticipantId = Column(UUID, nullable=False)
    RoomId = Column(UUID, nullable=False)
    Policy = Column(Integer, nullable=False)

    Readers_ = relationship('Readers', back_populates='RoomClaims')
    Characters_ = relationship('Characters', back_populates='RoomClaims')
    Rooms_ = relationship('Rooms', back_populates='RoomClaims')


class Votes(Base):
    __tablename__ = 'Votes'
    __table_args__ = (
        ForeignKeyConstraint(['GameId'], ['Games.GameId'], ondelete='CASCADE', name='FK_Votes_Games_GameId'),
        ForeignKeyConstraint(['PostId'], ['Posts.PostId'], ondelete='CASCADE', name='FK_Votes_Posts_PostId'),
        ForeignKeyConstraint(['TargetUserId'], ['Users.UserId'], ondelete='CASCADE', name='FK_Votes_Users_TargetUserId'),
        ForeignKeyConstraint(['UserId'], ['Users.UserId'], ondelete='CASCADE', name='FK_Votes_Users_UserId'),
        PrimaryKeyConstraint('VoteId', name='PK_Votes'),
        Index('IX_Votes_GameId', 'GameId'),
        Index('IX_Votes_PostId', 'PostId'),
        Index('IX_Votes_TargetUserId', 'TargetUserId'),
        Index('IX_Votes_UserId', 'UserId')
    )

    VoteId = Column(UUID)
    PostId = Column(UUID, nullable=False)
    GameId = Column(UUID, nullable=False)
    UserId = Column(UUID, nullable=False)
    TargetUserId = Column(UUID, nullable=False)
    CreateDate = Column(DateTime(True), nullable=False)
    Type = Column(Integer, nullable=False)
    SignValue = Column(SmallInteger, nullable=False)

    Games_ = relationship('Games', back_populates='Votes')
    Posts_ = relationship('Posts', back_populates='Votes')
    Users_ = relationship('Users', foreign_keys=[TargetUserId], back_populates='Votes')
    Users1 = relationship('Users', foreign_keys=[UserId], back_populates='Votes_')

