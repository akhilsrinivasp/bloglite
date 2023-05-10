from flask_restful import Resource, reqparse, Api
from flask_jwt_extended import get_jwt_identity, jwt_required
from bloglite.models import User, users_schema, user_schema, Blog, blogs_schema, Follow, follows_schema
from bloglite import db
import json
import requests
from flask_jwt_extended import create_access_token, create_refresh_token, get_jwt_identity, jwt_required

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
        parser.add_argument('username', required=True)
        parser.add_argument('image', required=True)
        args = parser.parse_args()
        
        user = User.query.filter_by(username=get_jwt_identity()).first()
        if not user:
            return {'message': 'User {} doesn\'t exist'.format(get_jwt_identity())}, 404
        
        user.name = args['name']
        user.image = args['image']
        
        # if username is changed, update all blogs and follows
        if user.username != args['username']:
            user.username = args['username']
            blogs = Blog.query.filter_by(author=get_jwt_identity()).all()
            for blog in blogs:
                blog.author = args['username']
            follows = Follow.query.filter_by(follower=get_jwt_identity()).all()
            for follow in follows:
                follow.follower = args['username']
            follows = Follow.query.filter_by(following=get_jwt_identity()).all()
            for follow in follows:
                follow.following = args['username']
            access_token = create_access_token(identity=args['username'])
            refresh_token = create_refresh_token(identity=args['username'])
            return {
                'message': 'User {} was updated to {}'.format(get_jwt_identity(), args['username']),
                'access_token': access_token,
                'refresh_token': refresh_token
            }, 200
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

        