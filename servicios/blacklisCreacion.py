from entidades.blacklist import db, Blacklist, BlacklistModelSchema
from flask_jwt_extended import jwt_required
from servicios import servicioToken
from validaciones import validacionCuerpo

blacklist_Schema = BlacklistModelSchema()

response = {"mensaje": ""}


def get():
    token = servicioToken.crear_token(1)
    return token


@jwt_required
def post(request):
    errors = validacionCuerpo.validacion_atributos(request.json)
    if errors:
        response["mensaje"] = "La cuenta NO pudo ser creada."
        return response, 400

    blocked_reason: bool = False
    for valor in request.json.keys():
        if valor == "blocked_reason":
            blocked_reason = True

    try:
        blacklist = Blacklist(id_client=request.json['app_uuid'],
                              email=request.json['email'],
                              reason=request.json['blocked_reason'] if blocked_reason else " ",
                              ip_address=request.remote_addr)
        db.session.add(blacklist)
        db.session.commit()
    except:
        return response, 500

    response["mensaje"] = "La cuenta SI pudo ser creada."
    return response, 200
