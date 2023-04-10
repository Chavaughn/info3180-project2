import os
import subprocess
# Install required packages from requirements.txt
subprocess.call(['pip', 'install', '-r', 'requirements.txt'])
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config
from flask_wtf.csrf import CSRFProtect
from flask_cors import CORS
import time

app = Flask(__name__)
app.config.from_object(Config)
app.config['UPLOAD_FOLDER'] = os.path.abspath('./uploads/')
csrf = CSRFProtect(app)
db = SQLAlchemy(app)
cors = CORS(app)


from app import views