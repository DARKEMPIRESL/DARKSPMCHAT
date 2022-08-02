from sqlalchemy import Column, Integer, BigInteger, String, Boolean
from handlers.database import BASE, SESSION


class Users(BASE):
    __tablename__ = "users"
    __table_args__ = {'extend_existing': True}
    user_id = Column(Integer, primary_key=True)
    channels = Column(String, nullable=True)
    channel_id = Column(BigInteger, primary_key=True)
    force_chat = Column(BigInteger)
    action = Column(String)
    ignore_service = Column(Boolean)
    only_owner = Column(Boolean)

    def __init__(self, user_id, channel_id, force_chat, action='mute', ignore_service=True, only_owner=True):
        self.user_id = user_id
        self.channel_id = channel_id
        self.force_chat = force_chat
        self.action = action
        self.ignore_service = ignore_service
        self.only_owner = only_owner
        
    def __repr__(self):
        return "<User ({})>".format(self.user_id)


Users.__table__.create(checkfirst=True)
Chats.__table__.create(checkfirst=True)                       


def num_users():
    try:
        return SESSION.query(Users).count()
    finally:
        SESSION.close()
