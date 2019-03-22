from sqlalchemy import Column, Integer, String, DateTime, func, Boolean
from sqlalchemy.ext.declarative import declarative_base
from connection import create_db_session

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

    # @classmethod
    # def of(cls, name, id, password, email, phone):
    #     account = cls()
    #     account.user_name = name
    #     account.user_id = id
    #     account.user_password = password
    #     account.user_email = email
    #     account.user_phone = phone
    #     account.active = True
    #     return account

    @classmethod
    def alternative_init(cls):
        return cls()

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



if __name__ == '__main__':
    session = create_db_session()
    # account = Accounts(user_no=0, user_name='전욱태', user_id='wooktae', user_password='1234', user_email='wook@gmail.com',
    #                    user_phone='010-2515-8129', is_active=True)
    account = Accounts.of('전욱태', 'wooktae2', '1234', 'wook@gmail.com', '010-2515-8129')
    session.add(account)
    session.commit()


