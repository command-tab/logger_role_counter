import os
import urllib
from flask import Flask

# Configure Flask
app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # We do not depend on this feature, so supress warnings about it
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # In-memory SQLite only

# Configure Flask-SQLAlchemy
from app.models import db
db.init_app(app)

from app.models.user import User
from app.models.organization import Organization
from app.models.logger import Logger
from app.models.logger_role import LoggerRole
