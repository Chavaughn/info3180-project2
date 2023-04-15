import os
import subprocess
# Install required packages from requirements.txt
# subprocess.call(['pip', 'install', '-r', 'requirements.txt'])
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config
from flask_wtf.csrf import CSRFProtect
from flask_cors import CORS
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager


app = Flask(__name__)
app.config.from_object(Config)
app.config['SECRET_KEY']='Som3$ec5etK*y'

app.config['UPLOAD_FOLDER'] = os.path.abspath('./uploads/')
app.config['ASSESTS_FOLDER'] = os.path.abspath('./src/assets/')

csrf = CSRFProtect(app)
db = SQLAlchemy(app)
jwt = JWTManager(app)

CORS(app, resources={r"/*": {"origins": "*"}}, allow_headers="*")




from app import views
from app import models
migrate = Migrate(app,db)