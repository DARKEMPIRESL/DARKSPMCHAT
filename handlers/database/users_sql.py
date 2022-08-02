from sqlalchemy import Column, BIGINT, String
from . import BASE, SESSION


class Users(BASE):
    __tablename__ = "users"
    __table_args__ = {'extend_existing': True}
    user_id = Column(BIGINT, primary_key=True)
    channels = Column(String, nullable=True)
    target_user = Column(JSON)

    def __init__(self, user_id, target_user=None):
        self.user_id = user_id
        self.target_user = target_user


Users.__table__.create(checkfirst=True)


async def num_users():
    try:
        return SESSION.query(Users).count()
    finally:
        SESSION.close()
