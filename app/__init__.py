from flask import Flask, json, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from sqlalchemy import Date, cast
from config import app_config
import pytz
from datetime import datetime


db = SQLAlchemy()
login_manager = LoginManager()


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    #app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    db.init_app(app)

    # temporary route
    @app.route('/')
    def hello_world():
        return 'Hello World ! I am back with db running .......!'

    login_manager.init_app(app)
    login_manager.login_message = 'You must be logged in to access this page'
    login_manager.login_view = 'auth.login'

    migrate = Migrate(app,db)

    from app import models

    @app.route('/ctis', methods=['POST'])
    def GetDepartments():
        tzlima = pytz.timezone("America/Lima") 
        date = datetime.now(tzlima).strftime("%Y-%m-%d")

        data = request.json
        if 'search-mysql' not in data:
            response = app.response_class(
             response = json.dumps({
                'status': 'fail',
                'message': 'search-mysql doest not exits on request',
		    }),
             status=400,
             mimetype='application/json'
            )
            return response 

        else:
            if data['search-mysql']['start-date'] < date:
                response = app.response_class(
                response = json.dumps({
                    'status': 'fail',
                    'message': 'start-date is less than the current',
                }),
                status = 400,
                mimetype = 'application/json'
                )
                return response 

            ModelCITs = models.CIT.query.filter(
                cast(models.CIT.FECHA, Date) >= data['search-mysql']['start-date'],
                models.CIT.IDSEDE == data['search-mysql']['sede-id'],
                models.CIT.IDAFILIADO == data['search-mysql']['affiliate-id']
            ).limit(data['search-mysql']['top-limit']).all()
            cits = [ cit.get_response() for cit in ModelCITs]

            response = app.response_class(
                response=json.dumps({
                    'status': 'success',
                    'message': 'successful data collection.',
                    'data':cits
                }),
                status=200,
                mimetype='application/json'
            )

            return response


    return app
