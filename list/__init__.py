from list import views
from flask import Flask
from .config import DevConfig
from flask_bootstrap import Bootstrap


# intializing application

app = Flask(__name__, instance_relative_config=True)

# Setting up configurations
app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')

#initializing Flask Extensions
bootstrap = Bootstrap(app)
