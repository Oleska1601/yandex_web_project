import datetime
import sqlalchemy
from werkzeug.security import generate_password_hash, check_password_hash

from .db_session import SqlAlchemyBase
from sqlalchemy import orm


class Results_Dog(SqlAlchemyBase):
    __tablename__ = 'results_dog'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    dog_1 = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    dog_2 = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    dog_3 = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    dog_4 = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    dog_5 = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    user_id = sqlalchemy.Column(sqlalchemy.Integer,
                                sqlalchemy.ForeignKey("users.id"))

    user = orm.relationship('User')

