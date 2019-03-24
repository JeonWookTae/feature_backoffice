from typing import NamedTuple

from sqlalchemy import Column, Integer, String, DateTime, func, Boolean
from sqlalchemy.ext.declarative import declarative_base
from backoffice.connection import create_db_session

Base = declarative_base()


class Accounts(Base):
    __tablename__ = 'accounts'

    user_no = Column(Integer, autoincrement=True, primary_key=True)
    user_name = Column(Integer, nullable=False)
    user_id = Column(Integer, nullable=False)
    user_password = Column(String, nullable=False)
    user_email = Column(String, nullable=False)
    user_phone = Column(String, nullable=False)
    create_at = Column(DateTime(), nullable=False, default=func.now())
    active = Column(Boolean(create_constraint=True), nullable=False)

    @classmethod
    def of(cls, name, id, password, email, phone):
        ob = cls()
        ob.user_name = name
        ob.user_id = id
        ob.user_password = password
        ob.user_email = email
        ob.user_phone = phone
        ob.active = True
        return ob

    def to_json(self):
        return {"user_no": self.user_no,
                "user_id": self.user_id,
                "user_email": self.user_email}


class User(NamedTuple):
    user_no: int
    user_id: str
    user_password: str
    user_name: str
    user_email: str
    user_phone: str
    authenticated: bool
    is_active: bool

    @classmethod
    def of(cls, acc: Accounts):
        cls.user_no = acc.user_no
        cls.user_id = acc.user_id
        cls.user_name = acc.user_name
        cls.user_email = acc.user_email
        cls.user_phone = acc.user_phone
        cls.user_password: str = acc.user_password
        cls.is_active = True if acc.active else False
        cls.authenticated = False
        return cls

    @classmethod
    def can_login(cls, password):
        return cls.user_password == password

    @classmethod
    def get_id(cls):
        return cls.user_id

    @classmethod
    def is_authenticated(cls):
        return cls.authenticated

    @classmethod
    def is_anonymous(cls):
        return False


if __name__ == '__main__':
    session = create_db_session()