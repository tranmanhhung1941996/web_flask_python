from flask import Flask
my_app = Flask(__name__)
#my_app.config.from_object(config)
my_app.debug = True
my_app.secret_key = 'somesuperdupersecretkey'
from app import views 
