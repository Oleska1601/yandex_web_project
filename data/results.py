import datetime
import sqlalchemy
from werkzeug.security import generate_password_hash, check_password_hash

from .db_session import SqlAlchemyBase
from sqlalchemy import orm


class Results(SqlAlchemyBase):
    __tablename__ = 'results'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    dog = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    drink = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    cat = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    chinchilla = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    user_id = sqlalchemy.Column(sqlalchemy.Integer,
                                sqlalchemy.ForeignKey("users.id"))

    user = orm.relationship('User')
