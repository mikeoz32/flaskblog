
from flask import Flask
from flask_jwt_extended import JWTManager

from flaskblog.model.user import User


def init_jwt(app: Flask):
    app.config['JWT_SECRET_KEY'] = "Some_secret_key"
    jwt = JWTManager(app)

    @jwt.user_identity_loader
    def user_identity_loader(user: User):
        return user.id

    @jwt.user_lookup_loader
    def user_lookup_loader(_jwt_header, jwt_data):
        identity = jwt_data['sub']
        return User.query.filter_by(id=identity).one_or_none()


