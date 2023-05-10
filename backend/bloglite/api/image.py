import os
import secrets
from hashlib import sha256
from flask import request, send_file
from flask_restful import Resource
from bloglite.models import User, Blog
from flask_jwt_extended import jwt_required


def get_image(filename):
    img_dir = os.path.join(os.path.dirname(os.path.abspath(__file__))[:-4], 'static/image_data')
    img_path = os.path.join(img_dir, filename)
    return img_path

class Image(Resource):
    def get(self, type_or_name):
        # here type is the picture 
        return send_file(get_image(type_or_name), mimetype='image/png')
    
    @jwt_required()
    def post(self, type_or_name):
        if not request.form:
            return {'message': 'No form found'}, 404
        if ('image' in request.files):
            image = request.files['image']
            while True:
                encoded = image.filename.encode()
                hsh = str(sha256(encoded).hexdigest())[5:15]
                hsh = hsh[5:15]    
                salt = secrets.token_hex(8)
                filename = type_or_name + hsh + salt
                usr_chk = User.query.filter_by(image=filename).first()
                blg_chk = Blog.query.filter_by(image=filename).first()
                if not usr_chk and not blg_chk:
                    break
            img_dir = os.path.join(os.path.dirname(os.path.abspath(__file__))[:-4], 'static/image_data')
            img_path = os.path.join(img_dir, filename)
            image.save(img_path)
            image = filename
            return {'image_name': image}, 200
        
        else:
            return {'message': 'No image found'}, 404

class ImageUpload(Resource):
    @jwt_required()
    def post(self):
        type = request.form['type']
        if ('image' in request.files):
            image = request.files['image']
            while True:
                encoded = image.filename.encode()
                hsh = str(sha256(encoded).hexdigest())[5:15]
                hsh = hsh[5:15]    
                salt = secrets.token_hex(8)
                filename = type + hsh + salt
                usr_chk = User.query.filter_by(image=filename).first()
                blg_chk = Blog.query.filter_by(image=filename).first()
                if not usr_chk and not blg_chk:
                    break
            img_dir = os.path.join(os.path.dirname(os.path.abspath(__file__))[:-4], 'static/image_data')
            img_path = os.path.join(img_dir, filename)
            image.save(img_path)
            image = filename
            return {'image_name': image}, 200
        
        else:
            return {'message': 'No image found'}, 404