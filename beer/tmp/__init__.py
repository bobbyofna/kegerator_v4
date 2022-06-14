import logging
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '6G8v0Y08HbpyvOUg'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:AcA!B3rree@localhost/flasksql'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:AcA!B3rree@127.0.0.1:5432/beerdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['SECURE_PROXY_SSL_HEADER'] = ('HTTP_X_FORWARDED_PROTO', 'https')
app.config['SESSION_COOKIE_SECURE'] = True
app.config['CSRF_COOKIE_SECURE'] = True
app.config['SECURE_SSL_REDIRECT'] = True

db = SQLAlchemy(app)

log_level = logging.DEBUG
#log_file = 'beerpi.log'
log_format = '%(levelname)s:%(asctime)s:%(filename)s:%(lineno)d:%(threadName)s] %(message)s'
logging.basicConfig(level=logging.DEBUG, format=log_format)

from beer import routes
