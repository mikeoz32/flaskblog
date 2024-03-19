from pydantic import PostgresDsn
from pydantic_settings import BaseSettings
from flask import Flask

class Config(BaseSettings):
    db_uri: PostgresDsn = "postgresql://postgres:postgres@localhost/flaskblog"


def init_config(app: Flask):
    config = Config()
    app.config['SQLALCHEMY_DATABASE_URI'] = str(config.db_uri)
