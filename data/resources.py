from flask import jsonify
from flask_restful import Resource, abort, reqparse

from data import db_session
from data.results import Results
from data.results_dog import Results_Dog
from data.results_drink import Results_Drink


def abort_if_info_not_found(results_id):
    session = db_session.create_session()
    tests = session.query(Results).get(results_id)
    if not tests:
        abort(404, message=f"Result {results_id} not found")


class ResultsResource(Resource):

    def get(self, results_id):
        abort_if_info_not_found(results_id)
        session = db_session.create_session()
        results = session.query(Results).get(results_id)
        return jsonify({'results': results.to_dict(
            only=('dog', 'drink', 'cat', 'chinchilla', 'user_id'))})

    def delete(self, results_id):
        abort_if_info_not_found(results_id)
        session = db_session.create_session()
        results = session.query(Results).get(results_id)
        session.delete(results)
        session.commit()
        return jsonify({'success': 'OK'})


class Results_DogListResource(Resource):
    def get(self):
        session = db_session.create_session()
        results = session.query(Results_Dog).all()
        return jsonify({'results_dog': [item.to_dict(
            only=('dog_1', 'dog_2', 'dog_3', 'dog_4', 'dog_5' 'user_id')) for item in results]})

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('id', required=True, type=int)
        parser.add_argument('dog_1', required=True)
        parser.add_argument('dog_2', required=True)
        parser.add_argument('dog_3', required=True)
        parser.add_argument('dog_4', required=True)
        parser.add_argument('dog_5', required=True)
        parser.add_argument('user_id', required=True, type=int)
        args = parser.parse_args()
        session = db_session.create_session()
        results = Results_Dog(
            id=args['id'],
            dog_1=args['dog_1'],
            dog_2=args['dog_2'],
            dog_3=args['dog_3'],
            dog_4=args['dog_4'],
            dog_5=args['dog_5'],
            user_id=args['user_id']
        )
        session.add(results)
        session.commit()
        return jsonify({'success': 'OK'})


class Results_DrinkListResource(Resource):
    def get(self):
        session = db_session.create_session()
        results = session.query(Results_Drink).all()
        return jsonify({'results_drink': [item.to_dict(
            only=('drink_1', 'drink_2', 'drink_3', 'drink_4', 'drink_5' 'user_id')) for item in results]})

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('id', required=True, type=int)
        parser.add_argument('drink_1', required=True)
        parser.add_argument('drink_2', required=True)
        parser.add_argument('drink_3', required=True)
        parser.add_argument('drink_4', required=True)
        parser.add_argument('drink_5', required=True)
        parser.add_argument('user_id', required=True, type=int)
        args = parser.parse_args()
        session = db_session.create_session()
        results = Results_Drink(
            id=args['id'],
            drink_1=args['drink_1'],
            drink_2=args['drink_2'],
            drink_3=args['drink_3'],
            drink_4=args['drink_4'],
            drink_5=args['drink_5'],
            user_id=args['user_id']
        )
        session.add(results)
        session.commit()
        return jsonify({'success': 'OK'})


# на будущее


# class Results_CatListResource(Resource):
#     def get(self):
#         session = db_session.create_session()
#         results = session.query(Results_Cat).all()
#         return jsonify({'results_cat': [item.to_dict(
#             only=('cat_1', 'cat_2', 'cat_3', 'cat_4', 'cat_5' 'user_id')) for item in results]})
#
#     def post(self):
#         parser = reqparse.RequestParser()
#         parser.add_argument('id', required=True, type=int)
#         parser.add_argument('cat_1', required=True)
#         parser.add_argument('cat_2', required=True)
#         parser.add_argument('cat_3', required=True)
#         parser.add_argument('cat_4', required=True)
#         parser.add_argument('cat_5', required=True)
#         parser.add_argument('user_id', required=True, type=int)
#         args = parser.parse_args()
#         session = db_session.create_session()
#         results = Results_Drink(
#             id=args['id'],
#             cat_1=args['cat_1'],
#             cat_2=args['cat_2'],
#             cat_3=args['cat_3'],
#             cat_4=args['cat_4'],
#             cat_5=args['cat_5'],
#             user_id=args['user_id']
#         )
#         session.add(results)
#         session.commit()
#         return jsonify({'success': 'OK'})


# class Results_ChinchillaListResource(Resource):
#     def get(self):
#         session = db_session.create_session()
#         results = session.query(Results_Chinchilla).all()
#         return jsonify({'results_chinchilla': [item.to_dict(
#             only=('chinchilla_1', 'chinchilla_2', 'chinchilla_3', 'chinchilla_4', 'chinchilla_5' 'user_id')) for item in results]})
#
#     def post(self):
#         parser = reqparse.RequestParser()
#         parser.add_argument('id', required=True, type=int)
#         parser.add_argument('chinchilla_1', required=True)
#         parser.add_argument('chinchilla_2', required=True)
#         parser.add_argument('chinchilla_3', required=True)
#         parser.add_argument('chinchilla_4', required=True)
#         parser.add_argument('chinchilla_5', required=True)
#         parser.add_argument('user_id', required=True, type=int)
#         args = parser.parse_args()
#         session = db_session.create_session()
#         results = Results_Drink(
#             id=args['id'],
#             chinchilla_1=args['chinchilla_1'],
#             chinchilla_2=args['chinchilla_2'],
#             chinchilla_3=args['chinchilla_3'],
#             chinchilla_4=args['chinchilla_4'],
#             chinchilla_5=args['chinchilla_5'],
#             user_id=args['user_id']
#         )
#         session.add(results)
#         session.commit()
#         return jsonify({'success': 'OK'})