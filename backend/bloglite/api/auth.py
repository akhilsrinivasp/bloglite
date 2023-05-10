from flask_restful import Resource, reqparse
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, create_refresh_token, get_jwt_identity, jwt_required
from flask import request

import os
import secrets  
from hashlib import sha256
from flask import request
from flask_restful import Resource
from bloglite.models import User, Blog

from bloglite.models import User
from bloglite import db

class Register(Resource):
    def post(self):
        # parser = reqparse.RequestParser()
        # parser.add_argument('name', required=True)
        # parser.add_argument('username', required=True)
        # parser.add_argument('password', required=True)
        # parser.add_argument('email', required=True)
        # parser.add_argument('image', required=False, location='files')
        # args = parser.parse_args()
        
        # name = args['name']
        # username = args['username']
        # password = args['password']
        # email = args['email']
         
        # if args['image']:
        #     image = request.files['image']
            
        # # send a self request to /image of this flask server to upload the image
        # # and get the image name 
        # image = requests.post('http://localhost:5000/image/dp', files={'image': image})
        # image = image.json()['image_name']
        if not request.form:
            return {'message': 'No data found'}, 404
        data = request.form
        name = data['name']
        username = data['username']
        password = data['password']
        email = data['email']
        if ('image' in request.files):
            image = request.files['image']
            while(True):
                encoded = image.filename.encode()
                hsh = str(sha256(encoded).hexdigest())[5:15]
                hsh = hsh[5:15]    
                salt = secrets.token_hex(8)
                filename = "dp" + hsh + salt
                usr_chk = User.query.filter_by(image=filename).first()
                blg_chk = Blog.query.filter_by(image=filename).first()
                if not usr_chk and not blg_chk:
                    break
            
            img_dir = os.path.join(os.path.dirname(os.path.abspath(__file__))[:-4], 'static/image_data')
            img_path = os.path.join(img_dir, filename)
            image.save(img_path)
            image = filename
        else :
            image = "noimage"
    
        user = User.query.filter_by(username=username).first()
        if user:
            return {'message': 'User {} already exists'.format(username)}, 409
        
        new_user = User(
            name=name,
            username=username,
            password=generate_password_hash(password),
            email=email,
            image=image
        )
        
        db.session.add(new_user)
        db.session.commit()
        return {'message': 'User {} was created'.format(username)}, 201
    
class Login(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', required=True)
        parser.add_argument('password', required=True)
        args = parser.parse_args()
        
        username = args['username']
        password = args['password']
        
        user = User.query.filter_by(username=username).first()
        if not user:
            return {'message': 'User {} doesn\'t exist'.format(username)}, 404
        
        if check_password_hash(user.password, password):
            access_token = create_access_token(identity=username)
            refresh_token = create_refresh_token(identity=username)
            return {
                'message': 'Logged in as {}'.format(user.username),
                'access_token': access_token,
                'refresh_token': refresh_token
            }, 200
        else:
            return {'message': 'Wrong credentials'}, 401
        
class Refresh(Resource):
    @jwt_required(refresh=True)
    def post(self):
        username = get_jwt_identity()
        access_token = create_access_token(identity=username)
        refresh_token = create_refresh_token(identity=username)
        
        return {
            'message': 'Access token refreshed for {}'.format(username),
            'access_token': access_token,
            'refresh_token': refresh_token
        }, 200
        
class PasswordReset(Resource):
    @jwt_required()
    def put(self):
        parser = reqparse.RequestParser()
        parser.add_argument('new_password', required=True)
        parser.add_argument('old_password', required=True)
        args = parser.parse_args()
        
        new_password = args['new_password']
        old_password = args['old_password']
        
        user = User.query.filter_by(username=get_jwt_identity()).first()
        if not user:
            return {'message': 'User {} doesn\'t exist'.format(get_jwt_identity())}, 404
        
        if check_password_hash(user.password, old_password):
            user.password = generate_password_hash(new_password)
            db.session.commit()
            return {'message': 'Password updated'}, 200
        else:
            return {'message': 'Wrong credentials'}, 401