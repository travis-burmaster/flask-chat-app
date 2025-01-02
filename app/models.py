from flask_login import UserMixin
from . import login_manager

class User(UserMixin):
    _users = {}  # In-memory storage

    def __init__(self, id_, name, email):
        self.id = id_
        self.name = name
        self.email = email

    @staticmethod
    def get_or_create(token_data):
        user_id = token_data.get('oid') or token_data.get('sub')
        if not user_id:
            user_id = 1
            user = User(
                id_=1,
                name='Travis',
                email='azure@burmaster.com'
             )
            User._users[user_id] = user
            #raise ValueError("No user ID found in token data")
        
        if user_id not in User._users:
            user = User(
                id_=user_id,
                name=token_data.get('name', ''),
                email=token_data.get('preferred_username', '')
            )
            User._users[user_id] = user
        return User._users[user_id]

    @staticmethod
    def get(user_id):
        return User._users.get(user_id)

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)