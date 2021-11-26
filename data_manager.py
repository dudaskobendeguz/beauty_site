import connection
from time import time

USER_PATH = 'database/user.csv'
USER_HEADER = ['user_id', 'admin', 'email', 'username', 'birthday']
LOGGED_IN_USER_PATH = 'database/logged_in_user.csv'


def open_csv_file(file_path: str):
    return connection.open_csv_file(file_path)


def save_csv_file(data_list: list[dict], file_path: str, header: str):
    connection.save_csv_file(data_list, file_path, header)


def add_user(new_user: dict):
    users = open_csv_file(USER_PATH)
    users.append(new_user)
    save_csv_file(users, USER_PATH, USER_HEADER)


def login(user):
    user = [user]
    connection.save_csv_file(user, LOGGED_IN_USER_PATH, USER_HEADER)


def logout():
    connection.save_csv_file([], LOGGED_IN_USER_PATH, USER_HEADER)


def validate_login(username):
    users = open_csv_file(USER_PATH)
    for user in users:
        if username == user["username"]:
            login(user)
            return user
        else:
            return None


def logged_in_user():
    user = connection.open_csv_file(LOGGED_IN_USER_PATH)
    if len(user) >= 1:
        return user[0]
    else:
        return None

