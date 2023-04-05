from flask_jwt_extended import create_access_token


def crear_token(id):
    print("entro al tokem")
    token = create_access_token(identity=id)
    return token
