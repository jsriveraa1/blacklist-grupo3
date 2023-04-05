# import os
from flask import Flask, jsonify, request
# from flask_restful import Api
from flask_jwt_extended import JWTManager
from servicios import blacklistSalud, blacklisCreacion, blackList
# from adaptadores import conectorPostgres
from entidades.blacklist import db

application = Flask(__name__)

application.config[
    'SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@monitor-blacklists.ca3szrotq4rt.us-east-1.rds.amazonaws.com/postgres'
application.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app_context = application.app_context()
app_context.push()
db.init_app(application)
db.create_all()

application.config['JWT_SECRET_KEY'] = 'prueba'
JWT_ACCESS_TOKEN_EXPIRES = False
application.config['PROPAGATE_EXCEPTIONS'] = True


# api = Api(app)


@application.route("/")
def index():
    return jsonify(blacklistSalud.get())


@application.route("/blacklists", methods=["POST"])
def blacklists_create():
    return blacklisCreacion.post(request)


@application.route("/blacklists", methods=["GET"])
def blacklists_token():
    return blacklisCreacion.get()


@application.route("/blacklists/<string:email>")
def blacklists_list(email):
    return blackList.get(email)


jwt = JWTManager(application)

if __name__ == "__main__":
    application.run(port=5000, debug=True)
