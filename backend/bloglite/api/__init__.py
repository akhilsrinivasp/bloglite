from bloglite.api.user import UserAPI, DummyAPI, UserPublic
from bloglite.api.image import Image, ImageUpload
from bloglite.api.auth import Register, Login, Refresh, PasswordReset
from bloglite.api.follow import FollowAPI, UnFollowAPI, Following, Followers
from bloglite.api.blog import BlogAPI, PublicFeed, UserFeed, GetBlog

def register_api(api):
    api.add_resource(UserAPI, '/api/v1/user')
    api.add_resource(UserPublic, '/api/v1/user/<string:username>')
    api.add_resource(Image, '/api/v1/image/<string:type_or_name>')
    api.add_resource(ImageUpload, '/api/v1/image')
    api.add_resource(Register, '/api/v1/register')
    api.add_resource(Login, '/api/v1/login')
    api.add_resource(Refresh, '/api/v1/refresh')
    api.add_resource(PasswordReset, '/api/v1/password/reset')
    api.add_resource(FollowAPI, '/api/v1/follow')
    api.add_resource(UnFollowAPI, '/api/v1/unfollow')
    api.add_resource(Following, '/api/v1/following')
    api.add_resource(Followers, '/api/v1/followers')
    api.add_resource(BlogAPI, '/api/v1/blog')
    api.add_resource(GetBlog, '/api/v1/blog/<int:id>')
    api.add_resource(PublicFeed, '/api/v1/public')
    api.add_resource(UserFeed, '/api/v1/user/feed')
    
    api.add_resource(DummyAPI, '/api/v1/dummy')
    
    return api