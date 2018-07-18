from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
import os

from config import Config

pjdir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__, template_folder='templates', instance_relative_config=True)
app.config.from_object(Config)
# app.config.from_pyfile('config.py')

# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(pjdir, 'static/data/data_register.sqlite')
# app.config['SECRET_KEY']='testXXX'

bootstrap = Bootstrap(app)
db = SQLAlchemy(app)

from app_blog.author import view