from time import time
import data_manager


def register(email, admin=False):
    new_user = {
        'user_id': time(),
        'admin': admin,
        'email': email
    }
    data_manager.add_user(new_user)
    return new_user


