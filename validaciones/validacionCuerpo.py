import json

from marshmallow import Schema, fields, validates, ValidationError, validate


def validacion_atributos(parametros_enviados: {json}):
    errors = AddBodyRequestSchema().validate(parametros_enviados)
    return errors


class AddBodyRequestSchema(Schema):
    email = fields.Str(required=True, validate=validate.Email(error="Correo electronico invalido."))
    app_uuid = fields.Str(required=True,
                          validate=validate.Length(36, 36, error="Valor errado: El código UUID es errado."))
    blocked_reason = fields.Str(
        validate=validate.Length(1, 255, error="Value error: Longitud del campo es máximo 255 caracteres."))
