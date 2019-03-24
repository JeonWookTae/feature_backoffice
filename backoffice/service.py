from backoffice.domain.model import Accounts
from backoffice.connection import get_session


class User(object):
    user_no: int
    user_id: str
    user_name: str
    avatar = str
    user_dept: str
    user_email: str
    user_phone: str
    #is_active: bool

    def __init__(self, acc: Accounts):
        self.user_no = acc.user_no
        self.user_id = acc.user_id
        self.user_name = acc.user_name
        self.user_email = acc.user_email
        self.user_phone = acc.user_phone
        self.created_at = acc.create_at
        #self.is_active = acc.active
        self.password = acc.user_password
        self.authenticated = False

    def can_login(self, passwd_hash):
        return self.password == passwd_hash

    def is_active(self):
        return True

    def get_id(self):
        return self.user_id

    def is_authenticated(self):
        return self.authenticated

    def is_anonymous(self):
        return False


def sing_up(user):
    # name, id, password, email, phone
    account = Accounts.of(user.get('name'),
                          user.get('id'),
                          user.get('password'),
                          user.get('email'),
                          user.get('phone'))
    with get_session() as session:
        session.add(account)
    return {'ok': 200, 'msg': 'success'}


def user_load(login):
    login_id = login.get('id')
    login_password = login.get('password')
    with get_session() as session:
        our_user = session.query(Accounts).filter_by(user_id=login_id, user_password=login_password).first()
        if our_user:
            return User(our_user)
        else:
            return None


if __name__ == '__main__':
    user = {'name': '홍길동',
            'id': 'hong',
            'password': '12345',
            'email': 'hong@gmail.com',
            'phone': '010-1234-1234'}
    # sing_up(user=user)
    print(user_load(login=user))
