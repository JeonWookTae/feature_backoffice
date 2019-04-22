from flask_login import login_user
from flask import jsonify

from backoffice.domain.model import Accounts, User
from backoffice.connection import get_session


def unauthorized_return():
    return jsonify({'ok': 404, 'msg': 'unauthorized'})


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


# def user_load(login):
#     login_id = login.get('id')
#     login_password = login.get('password')
#     with get_session() as session:
#         our_user = session.query(Accounts).filter_by(user_id=login_id, user_password=login_password).first()
#         if our_user:
#             return User.of(our_user)
#         else:
#             return None


def user_id_load(login):
    login_id = login
    with get_session() as session:
        our_user = session.query(Accounts).filter_by(user_id=login_id).first()
        if our_user:
            return User.of(our_user)
        else:
            return None


def user_authenticated(login_result, result_bool):
    login_result.authenticated = result_bool
    login_user(login_result, remember=result_bool)


def user_id_valid_check(login_result: User):
    if login_result:
        user_authenticated(login_result, True)
        return {"ok": 200, "msg": "success"}
    return {"ok": 401, "msg": "Invalid user_id or password"}


def user_password_valid_check(login_result: User, user_password):
    if login_result.can_login(user_password):
        user_authenticated(login_result, False)
        return {"ok": 402, "msg": "Invalid password"}
    return {"ok": 200, "msg": "success"}


def user_login_valid_check(user_id, user_password):
    login_result = user_id_load(user_id)
    valid = user_id_valid_check(login_result)
    if valid.get("ok") == 200:
        valid = user_password_valid_check(login_result, user_password)
    return valid


if __name__ == '__main__':
    user = {'name': '홍길동',
            'id': 'hong',
            'password': '12345',
            'email': 'hong@gmail.com',
            'phone': '010-1234-1234'}
    # sing_up(user=user)
    # print(user_load(login=user))
