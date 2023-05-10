from flask_restful import Resource, reqparse, Api
from flask_jwt_extended import get_jwt_identity, jwt_required
from bloglite.models import User, Blog, Follow, user_schema, blog_schema, follow_schema, users_schema, blogs_schema, follows_schema
from bloglite import db

import os
import secrets  
from hashlib import sha256
from flask import request

class GetBlog(Resource):
    def get(self, id):
        blog = Blog.query.filter_by(id=id).first()
        if not blog:
            return {'message': 'Blog {} doesn\'t exist'.format(id)}, 404
        
        blog = blog_schema.dump(blog)
        return blog, 200

class BlogAPI(Resource):
    @jwt_required()
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('id', required=True)
        args = parser.parse_args()
        
        blog = Blog.query.filter_by(id=args['id']).first()
        if not blog:
            return {'message': 'Blog {} doesn\'t exist'.format(args['id'])}, 404
        
        blog = blog_schema.dump(blog)
        return blog, 200
    
    @jwt_required()
    def post(self):
        data = request.form
        
        if not data['title'] or not data['content']:
            return {'message': 'Title or content is missing'}, 404
    
        if ('image' in request.files):
            image = request.files['image']
            while True:
                encoded = image.filename.encode()
                hsh = str(sha256(encoded).hexdigest())[5:15]
                hsh = hsh[5:15]    
                salt = secrets.token_hex(8)
                filename = "post" + hsh + salt
                usr_chk = User.query.filter_by(image=filename).first()
                blg_chk = Blog.query.filter_by(image=filename).first()
                if not usr_chk and not blg_chk:
                    break
            img_dir = os.path.join(os.path.dirname(os.path.abspath(__file__))[:-4], 'static/image_data')
            img_path = os.path.join(img_dir, filename)
            image.save(img_path)
            image = filename
        else :
            return {'message': 'Image not found'}, 404
        
        user = User.query.filter_by(username=get_jwt_identity()).first()
        if not user:
            return {'message': 'User {} doesn\'t exist'.format(get_jwt_identity())}, 404
        
        new_blog = Blog(
            title= data['title'],
            content= data['content'],
            image=image,
            author=user.username,
        )
        
        db.session.add(new_blog)
        db.session.commit()
        return {'message': 'Blog {} was created'.format(new_blog.title)}, 201
        
    @jwt_required()
    def put(self):
        parser = reqparse.RequestParser()
        parser.add_argument('id', required=True)
        parser.add_argument('title', required=True)
        parser.add_argument('content', required=True)
        args = parser.parse_args()
        
        user = User.query.filter_by(username=get_jwt_identity()).first()
        if not user:
            return {'message': 'User {} doesn\'t exist'.format(get_jwt_identity())}, 404
        
        blog = Blog.query.filter_by(id = args['id']).first()
        if not blog:
            return {'message': 'Blog {} doesn\'t exist'.format(get_jwt_identity())}, 404
        
        blog.title = args['title']
        blog.content = args['content']
        
        db.session.commit()
        return {'message': 'Blog {} was updated'.format(get_jwt_identity())}, 200
    
    @jwt_required()
    def delete(self):
        parser = reqparse.RequestParser()
        parser.add_argument('id', required=True)
        args = parser.parse_args()
        
        user = User.query.filter_by(username=get_jwt_identity()).first()
        if not user:
            return {'message': 'User {} doesn\'t exist'.format(get_jwt_identity())}, 404
        
        blog = Blog.query.filter_by(id=args['id']).first()
        if not blog:
            return {'message': 'Blog doesn\'t exist'}, 404
        
        db.session.delete(blog)
        db.session.commit()
        return {'message': 'Blog {} was deleted'.format(blog.title)}, 200

class PublicFeed(Resource):   
    def get(self):
        blogs = Blog.query.order_by(Blog.created_at.desc()).limit(10).all()
        return blogs_schema.dump(blogs), 200
    
class UserFeed(Resource):
    @jwt_required()
    def get(self):
        username = get_jwt_identity()
        # join the Blog and Follow table
        blogs = Blog.query.join(Follow, Follow.following == Blog.author).filter(Follow.follower == username).order_by(Blog.created_at.desc()).limit(50).all()
        following = Follow.query.filter_by(follower=username).all()
        # if not blogs:
        #     return {'message': 'No blogs found'}, 404
        # return blogs_schema.dump(blogs), 200
        return blogs_schema.dump(blogs), 200
