from . import db, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash

#Create new users
class User(db.Model,UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255),unique = True, index=True)
    password = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True, index=True)
    secure_password = db.Column(db.String(255))
    bio = db.Column(db.String(255))
    profile_pic = db.Column(db.String())

    @property
    def set_password(self):
        raise AttributeError("You cannot read password attribute")

    @set_password.setter
    def password(self, password):
        self.secure_password = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.secure_password, password)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

# # User Authentification
#     @property
#     def password(self):
#         raise AttributeError("You cannot read the password")
#
#     @password.setter
#     def set_password(self, password):
#         password_hash = generate_password_hash(password)
#         self.password = password_hash
#
#     def verify_password(self, password):
#         return check_password_hash(self.password, password)

    def __repr__(self):
        return f'User {self.username}'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))