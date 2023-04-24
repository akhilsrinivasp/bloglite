from bloglite.database import db, ma
from sqlalchemy.sql import func 

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    image = db.Column(db.String(80), unique=False, nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    updated_at = db.Column(db.DateTime(timezone=True), onupdate=func.now())
    
    def __init__(self, name, username, email, password, image):
        self.name = name
        self.username = username
        self.email = email
        self.password = password
        self.image = image
    
    def __repr__(self):
        return '<User %r>' % self.username
    
    def following(self):
        count = Follow.query.filter_by(follower=self.username).count()
        following = Follow.query.filter_by(follower=self.username).all()
        return [count, follows_schema.dump(following)]
    
    def followers(self):
        count = Follow.query.filter_by(following=self.username).count()
        followers = Follow.query.filter_by(following=self.username).all()
        return [count, follows_schema.dump(followers)]
    
class Blog(db.Model):
    __tablename__ = 'blog'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    content = db.Column(db.String(1500), nullable=False)
    image = db.Column(db.String(80), unique=True, nullable=False)
    author = db.Column(db.String(80), db.ForeignKey('user.username'), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    updated_at = db.Column(db.DateTime(timezone=True), onupdate=func.now())
    db.relationship('User', backref=db.backref('blog', lazy=True))
    
    def __init__(self, title, content, image, author):
        self.title = title
        self.content = content
        self.image = image
        self.author = author
    
    def __repr__(self):
        return '<Blog %r>' % self.title    
    
class Follow(db.Model):
    __tablename__ = 'follow'
    id = db.Column(db.Integer, primary_key=True)
    follower = db.Column(db.String(80), db.ForeignKey('user.username'), unique=False, nullable=False)
    following = db.Column(db.String(80), db.ForeignKey('user.username'), unique=False, nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    updated_at = db.Column(db.DateTime(timezone=True), onupdate=func.now())
    db.relationship('User', backref=db.backref('follow', lazy=True))
    
    def __init__(self, follower, following):
        self.follower = follower
        self.following = following
    
    def __repr__(self):
        return '<Follows %r>' % self.follower
    
class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'username', 'email', 'image', 'created_at', 'updated_at')

class BlogSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'content', 'image', 'author', 'created_at', 'updated_at')
        
class FollowsSchema(ma.Schema):
    class Meta:
        fields = ('id', 'follower', 'following', 'created_at', 'updated_at')
        
user_schema = UserSchema()
users_schema = UserSchema(many=True)
blog_schema = BlogSchema()
blogs_schema = BlogSchema(many=True)
follow_schema = FollowsSchema()
follows_schema = FollowsSchema(many=True)
