from flask_login import UserMixin
from . import login_manager

class User(UserMixin):
    def __init__(self, id_, name, email):
        self.id = id_
        self.name = name
        self.email = email

    @staticmethod
    def get_or_create(token_data):
        user_id = token_data['oid']
        user = User(
            id_=user_id,
            name=token_data.get('name', ''),
            email=token_data.get('preferred_username', '')
        )
        return user

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)