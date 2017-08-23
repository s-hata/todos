import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

config = 'app.config.' + os.getenv('ENV', 'Development')
app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)

from app import resources
