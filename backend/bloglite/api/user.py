from flask_restful import Resource, reqparse, Api
from flask_jwt_extended import get_jwt_identity, jwt_required
from bloglite.models import User, users_schema, user_schema, Blog, blogs_schema, Follow, follows_schema
from bloglite import db
import json

class UserAPI(Resource):
    @jwt_required()
    def get(self):
        user = User.query.filter_by(username=get_jwt_identity()).first()
        if not user:
            return {'message': 'User {} doesn\'t exist'.format(get_jwt_identity())}, 404
        
        user = user_schema.dump(user)
        return user, 200
        
    @jwt_required()
    def put(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', required=True)
        parser.add_argument('email', required=True)
        parser.add_argument('image', required=True)
        args = parser.parse_args()
        
        user = User.query.filter_by(username=get_jwt_identity()).first()
        if not user:
            return {'message': 'User {} doesn\'t exist'.format(get_jwt_identity())}, 404
        
        user.name = args['name']
        user.email = args['email']
        user.image = args['image']
        
        db.session.commit()
        return {'message': 'User {} was updated'.format(get_jwt_identity())}, 200
    
class DummyAPI(Resource):
    def get(self):
        users = User.query.all()
        return users_schema.dump(users), 200
    
class UserPublic(Resource):
    def get(self, username): 
        user = User.query.filter_by(username=username).first()
        blogs = Blog.query.filter_by(author=username).all()
        if not user:
            return {'message': 'User {} doesn\'t exist'.format(username)}, 404
        follows = user.following()
        followers = user.followers()
        response = {
            'user': user_schema.dump(user),
            'blogs': blogs_schema.dump(blogs),
            'follows': follows[1],
            'followers': followers[1],
            'follow_count': follows[0],
            'followers_count': followers[0]
        }
        # response = json.dumps(response)
        return response, 200

        