from flask_restful import Resource, reqparse, Api
from flask_jwt_extended import get_jwt_identity, jwt_required
from bloglite.models import User, Follow, user_schema, users_schema, follow_schema, follows_schema
from bloglite import db

class Following(Resource):
    @jwt_required()
    def get(self):
        user = User.query.filter_by(username=get_jwt_identity()).first()
        if not user:
            return {'message': 'User {} doesn\'t exist'.format(get_jwt_identity())}, 404
        # use join operation to get followers along with the following details
        user_is_following = User.query.join(Follow, Follow.following == User.username).filter(Follow.follower == user.username).all()
        user_is_following = users_schema.dump(user_is_following)
        length = len(user_is_following)
        res = {'length': length, 'users': user_is_following}
        return res, 200
    
class Followers(Resource): 
    @jwt_required()
    def get(self):
        user = User.query.filter_by(username=get_jwt_identity()).first()
        if not user:
            return {'message': 'User {} doesn\'t exist'.format(get_jwt_identity())}, 404
        # use join operation to get followers along with the following details
        user_followers = User.query.join(Follow, Follow.follower == User.username).filter(Follow.following == user.username).all()
        user_followers = users_schema.dump(user_followers)
        length = len(user_followers)
        res = {'length': length, 'users': user_followers}
        return res, 200
    
class FollowAPI(Resource):
    @jwt_required()
    def post(self):
        username = get_jwt_identity()
        parser = reqparse.RequestParser()
        parser.add_argument('following', required=True)
        args = parser.parse_args()
        
        user = User.query.filter_by(username=username).first()
        if not user:
            return {'message': 'User {} doesn\'t exist'.format(username)}, 404
        
        follower = User.query.filter_by(username=args['following']).first()
        if not follower:
            return {'message': 'User {} doesn\'t exist'.format(args['following'])}, 404
        
        if user.id == follower.id:
            return {'message': 'You cannot follow yourself'}, 400
        
        follow = Follow.query.filter_by(follower=user.username, following=follower.username).first()
        if follow:
            return {'message': 'You already follow this user'}, 400
        
        new_follow = Follow(
            follower= user.username,
            following = follower.username,
        )
        db.session.add(new_follow)
        db.session.commit()
        
        return {'message': 'You are now following {}'.format(follower.username)}, 200
    
class UnFollowAPI(Resource):
    @jwt_required()
    def delete(self):
        username = get_jwt_identity()
        parser = reqparse.RequestParser()
        parser.add_argument('following', required=True)
        args = parser.parse_args()
        
        user = User.query.filter_by(username=username).first()
        if not user:
            return {'message': 'User {} doesn\'t exist'.format(username)}, 404
        
        follower = User.query.filter_by(username=args['following']).first()
        if not follower:
            return {'message': 'User {} doesn\'t exist'.format(args['following'])}, 404
        
        if user.id == follower.id:
            return {'message': 'You cannot unfollow yourself'}, 400
        
        follow = Follow.query.filter_by(follower=user.username, following=follower.username).first()
        if not follow:
            return {'message': 'You don\'t follow this user'}, 400
        
        db.session.delete(follow)
        db.session.commit()
        
        return {'message': 'You are no longer following {}'.format(follower.username)}, 200
        