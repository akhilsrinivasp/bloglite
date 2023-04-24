import os
import secrets
from hashlib import sha256
from flask import request, send_file
from flask_restful import Resource
from bloglite.models import User, Blog


def get_image(filename):
    img_dir = os.path.join(os.path.dirname(os.path.abspath(__file__))[:-4], 'static/image_data')
    img_path = os.path.join(img_dir, filename)
    return img_path
    
def put_image(type, image):
    while(True):
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
    return filename

class Image(Resource):
    def post(self, type_or_name):
        if 'image' not in request.files:
            return {'message': 'No image found in the request'}, 400
        
        image = request.files['image']
        if image.filename == '':
            return {'message': '2. No image found in the request'}, 400
        
        if image:
            filename = put_image(type_or_name, image)
            return {'message': 'Image saved successfully', 'image_name': filename}, 200
        
    def get(self, type_or_name):
        # here type is the picture 
        return send_file(get_image(type_or_name), mimetype='image/png')
        

        
    