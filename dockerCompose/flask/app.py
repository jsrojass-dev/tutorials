import os
from flask import Flask


app = Flask(__name__)

@app.route('/about', methods=['GET'])
def about():
    version = os.environ.get('APP_VERSION')

    return {'version': version}, 200

@app.route('/secrets', methods=['GET'])
def secrets():
    credentials = dict()
    credentials['db_password'] = os.environ.get('DB_PASSWORD')
    credentials['app_token'] = os.environ.get('APP_TOKEN')
    credentials['api_key'] = open("/run/secrets/api_key","r").read()
    credentials['api_key_v2'] = open("/api_key.txt","r").read()

    return credentials, 200