from flask import Flask

from flaskblog.model import init_models
from flaskblog.config import init_config

app = Flask(__name__)

init_config(app)
init_models(app)
