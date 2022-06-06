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
            json_ = {}
            for cita in cits:
                date = cita["FECHA"].split("T")[0]
                if date in json_.keys():
                    json_[date].append(
                        cita
                    )
                else:
                    json_[date] = [
                        cita
                        ]
            response = app.response_class(
                response=json.dumps({
                    'status': 'success',
                    'message': 'successful data collection.',
                    'data': json_
                }),
                status=200,
                mimetype='application/json'
            )

            return response

    @app.route('/afis/docidafiliado', methods=['POST'])
    def Get_affiliate_by_docidafiliado():
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
            ModelAFI = models.AFI.query.filter(
                models.AFI.DOCIDAFILIADO == data['search-mysql']['docID-affiliate']
            ).first()

            if (ModelAFI is None):
                response = app.response_class(
                    response = json.dumps({
                        'status': 'fail',
                        'message': 'docID-affiliate does not exits',
                    }),
                    status=400,
                    mimetype='application/json'
                )
                return response 
            else:
                response = app.response_class(
                    response=json.dumps({
                        'status': 'success',
                        'message': 'successful data collection.',
                        'data': ModelAFI.get_response()
                    }),
                    status=200,
                    mimetype='application/json'
                )

                return response

    @app.route('/afis/idafiliado', methods=['POST'])
    def Get_affiliate_by_idafiliado():
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
            ModelAFI = models.AFI.query.filter(
                models.AFI.IDAFILIADO == data['search-mysql']['affiliateID']
            ).first()

            if (ModelAFI is None):
                response = app.response_class(
                    response = json.dumps({
                        'status': 'fail',
                        'message': 'affiliateID does not exits',
                    }),
                    status=400,
                    mimetype='application/json'
                )
                return response 
            else:
                response = app.response_class(
                    response=json.dumps({
                        'status': 'success',
                        'message': 'successful data collection.',
                        'data': ModelAFI.get_response()
                    }),
                    status=200,
                    mimetype='application/json'
                )

                return response
    
    @app.route('/affiliates/create', methods=['POST'])
    def Create_affiliate():
        data = request.json
        if 'create-mysql' not in data:
            response = app.response_class(
            response = json.dumps({
                'status': 'fail',
                'message': 'create-mysql doest not exits on request',
            }),
            status=400,
            mimetype='application/json'
            )
            return response 

        afi = models.AFI(
            TIPO_DOC=data['create-mysql']["typeDoc"],
            DOCIDAFILIADO=data['create-mysql']["numberDoc"],
            PNOMBRE=data['create-mysql']["firstName"],
            PAPELLIDO=data['create-mysql']["firstSurname"],
            SEXO=data['create-mysql']["gender"],
            IDTIPOAFILIACION=data['create-mysql']["iPS"],
            IDPLAN=data['create-mysql']["planID"],
            TELEFONORES=data['create-mysql']["phone"],
            DIRECCION=data['create-mysql']["address"],
            IDSEDE=data['create-mysql']["sedeID"]
        )
        db.session.add(afi)
        db.session.flush()
        db.session.commit()
        response = app.response_class(
            response=json.dumps({
                'status': 'success',
                'message': 'successful data collection.',
                'data': afi.get_response()
            }),
            status=200,
            mimetype='application/json'
        )
        return response
    return app
