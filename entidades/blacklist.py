import sqlalchemy
from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

db = SQLAlchemy()


class Blacklist(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_client = db.Column(db.String(39))
    email = db.Column(db.String(50))
    reason = db.Column(db.String(255))
    ip_address = db.Column(db.String(20))
    createdAt = db.Column(db.DateTime, default=sqlalchemy.func.now())


class BlacklistModelSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Blacklist
        include_relationships = True
        include_fk = True
        load_instance = True
