from entidades.blacklist import db, Blacklist, BlacklistModelSchema
from flask_jwt_extended import jwt_required
from flask import Flask, jsonify


blacklist_Schema = BlacklistModelSchema()

response = {"mensaje": ""}


@jwt_required
def get(email):
    if email is None:
        response["mensaje"] = "Para realizar la consulta hace falta ingresar el correo electronico."
        return jsonify(response), 400

    find_blacklists = db.session.query(Blacklist).filter(Blacklist.email == email).all()

    if not find_blacklists:
        response["mensaje"] = "El correo no se encuentra creado en la lista negras."
        return jsonify(response), 404

    return jsonify([blacklist_Schema.dump(blacklist) for blacklist in find_blacklists])
