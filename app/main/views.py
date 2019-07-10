from flask import render_template, request, redirect, url_for, abort, flash
from . import main
from ..email import mail_message
from .. import db,photos
from ..requests import get_quotes
from ..models import Blog, User, Comment
from flask_login import login_user, logout_user, login_required, current_user
from .forms import BlogForm, CommentForm,UpdateProfile


@main.route('/')
def index():

    blogs = Blog.query.all()
    print(blogs)
    quotes = get_quotes()
    print(quotes)
    if blogs is None:
        return redirect(url_for('main.new_blog'))
        flash("no blogs")
    return render_template("index.html", blogs=blogs,quotes = quotes)


@main.route('/new_blog', methods=['GET', 'POST'])
@login_required
def new_blog():
    form = BlogForm()
    if form.validate_on_submit():
        blog = Blog(blog=form.blog.data, blog_title=form.blog_title.data, user_id = current_user.id,
                    blog_upvotes=0, blog_downvotes=0)
        if current_user.subscribe == 1:
            mail_message("New blog","email/welcome_user",current_user.email,current_user=current_user)
            print('qwertyuiojpjxszmkl')        
        blog.save_blog
        db.session.add(blog)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('new_blog.html', blog_form=form)

@main.route("/blog/update/<int:id>", methods=['GET', 'POST'])
@login_required
def update_blog(id):
    blog = Blog.query.filter_by(id = id).first()
    print(blog)
    form = BlogForm()
    if form.validate_on_submit():
        blog = Blog(blog=form.blog.data, blog_title=form.blog_title.data, user_id = current_user.id,
                    blog_upvotes=0, blog_downvotes=0)
        db.session.commit()
        flash('Your Blog has been updated!', 'success')
        return redirect(url_for('main.index', blog_id=blog.id))
    elif request.method == 'GET':
        form.blog_title.data = blog.blog_title
        form.blog.data = blog.blog
    return render_template('new_blog.html',blog_form=form)


@main.route('/delete/new/<int:id>', methods=['GET','POST'])
def delete_blog(id):
    blog = Blog.query.filter_by(id=id).first()
    if blog is not None:
        blog.delete_blog()
        return redirect (url_for('main.index'))

    return render_template('index.html')


@main.route('/new_comment/<int:id>', methods=['GET', 'POST'])
@login_required
def new_comment(id):
    form = CommentForm()
    blog = Blog.get_blog(id)
    comments = Comment.get_comments(id)
    print(comments)
    if form.validate_on_submit():
        comment = Comment(comment=form.comment.data, blog_id=blog.id)
        db.session.add(comment)
        db.session.commit()
        return redirect(url_for('main.index'))
        title = "pitches"
    return render_template('new_comment.html', comment_form=form, comments=comments)

@main.route('/delete/new/<int:id>', methods=['GET','POST'])
def delete_comment(id):
    comment = Comment.query.filter_by(id=id).first()
    if comment is not None:
        comment.delete_comment()
        return redirect (url_for('main.index'))

    return render_template('index.html')


@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)


@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))





