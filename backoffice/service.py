from flask_login import login_user

from backoffice.domain.model import Accounts, User
from backoffice.connection import get_session


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
            return User.of(our_user)
        else:
            return None


def user_id_load(login):
    login_id = login
    with get_session() as session:
        our_user = session.query(Accounts).filter_by(user_id=login_id).first()
        if our_user:
            return User.of(our_user)
        else:
            return None


def user_login_valid_check(user_id, user_password):
    login_result = user_id_load(user_id)
    if login_result:
        login_result.authenticated = True
        login_user(login_result, remember=True)
        json_result = {"ok": True, 'msg': 'success'}
    elif login_result.can_login(password=user_password):
        json_result = {"ok": False, 'msg': 'Invalid user_id or password'}
    else:
        json_result = {"ok": False, 'msg': 'Invalid user_id or password'}
    return json_result


if __name__ == '__main__':
    user = {'name': '홍길동',
            'id': 'hong',
            'password': '12345',
            'email': 'hong@gmail.com',
            'phone': '010-1234-1234'}
    # sing_up(user=user)
    print(user_load(login=user))
