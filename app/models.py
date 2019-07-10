from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime
from . import login_manager


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(UserMixin, db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), index=True)
    email = db.Column(db.String(255), unique=True, index=True)
    bio = db.Column(db.String(255))
    subscribe = db.Column(db.Integer)
    profile_pic_path = db.Column(db.String())
    blog = db.relationship('Blog', backref='user', lazy="dynamic")
    password_hash = db.Column(db.String(255))
    role_id = db.Column(db.Integer)

    @property
    def password(self):
        raise AttributeError('You cannnot read the password attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def save_user(self):
        db.session.add(self)
        db.session.commit()
    
    @classmethod
    def get_user(cls, id):
        user = User.query.filter_by(id=id).first()
        return user

    def __repr__(self):
        return f'User {self.username}'





class Blog(db.Model):
    __tablename__ = 'blogs'
    id = db.Column(db.Integer, primary_key=True)
    blog_title = db.Column(db.String)
    blog = db.Column(db.String)
    blog_upvotes = db.Column(db.Integer)
    blog_downvotes = db.Column(db.Integer)
    posted = db.Column(db.Time, default=datetime.utcnow())
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    comment_id = db.relationship("Comment", backref="blogs", lazy="dynamic")

    def save_blog(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_blog(cls, id):
        blog = Blog.query.filter_by(id=id).first()
        return blog

    @classmethod
    def get_blogs(cls, id):
        blogs = Blog.query.filter_by(id=id).all()
        return blogs

    def delete_blog(self):
        db.session.delete(self)
        db.session.commit()

    


class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db. Integer, primary_key=True)
    comment = db.Column(db.String(255))
    posted = db.Column(db.DateTime, default=datetime.utcnow)
    blog_id = db.Column(db.Integer, db.ForeignKey("blogs.id"))

    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    def delete_comment(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def get_comments(self, id):
        comments = Comment.query.filter_by(blog_id =id).all()
        return comments
