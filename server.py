from flask import Flask
from flask import render_template, abort, make_response, redirect, url_for, flash
from flask import request, Response
from forms import BookmarkForm, LoginForm, SignupForm
from flask_login import LoginManager, login_required, login_user, logout_user, current_user

from logging import DEBUG

import os
from flask_sqlalchemy import SQLAlchemy
basedir = os.path.abspath(os.path.dirname(__file__))

application = Flask(__name__)
application.logger.setLevel(DEBUG)
application.config['SECRET_KEY'] = '\x97\xdd\xd3\xe6]b?D\xe0VQ\xd5\xff~g\xd2\xf3\x07#\x90\xf6\x1d\xcb\xf6'  
application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'statusapp.db')
db = SQLAlchemy(application)

login_manager = LoginManager()
login_manager.session_protection = "strong"
login_manager.login_view = "login"
login_manager.init_app(application)

@login_manager.user_loader
def load_user(userid):
    return User.query.get(userid)

from models import User, Bookmark

@application.route('/signup',methods=['GET','POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        user = User(email=form.email.data,
                    username=form.username.data,
                    password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Welcom {}! Please, login.'.format(user.username))
        return redirect(url_for('login'))
    return render_template('signup.html',form=form)


@application.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.get_by_username(username=form.username.data)
        if user is not None and user.check_password(form.password.data):
            login_user(user, form.remember_me.data)
            flash('Logged in successfully as {}'.format(user.username))
            return redirect(request.args.get('next') or url_for('user',username=user.username))
        flash('Incorrect username or password')
    return render_template('login.html',form=form)

@application.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('return_200'))

@application.route('/user/<username>')
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    return render_template('user.html',user=user)

@application.route('/add',methods=['GET','POST'])
@login_required
def add():
    form = BookmarkForm()
    if form.validate_on_submit():
        url = request.form['url']
        bm = Bookmark(user=current_user, url=url)
        db.session.add(bm)
        db.session.commit()
        application.logger.debug('URL:' + url)
        flash("Stored url: {}".format(url))
        return redirect(url_for('return_200'))
    return render_template('add.html',form=form)

@application.route('/100')
def return_100():
    print_request_info()
    return render_template('empty.html'),100

@application.route('/')
def return_200():
    bookmarks = Bookmark.newest(5)
    print_request_info()
    content = render_template('index.html',bookmarks=bookmarks)
    #application.logger.debug('content:' + content) 
    return make_response(content,200)

@application.route('/201')
def return_201():
    print_request_info()
    return render_template('empty.html'),201

@application.route('/202')
def return_202():
    print_request_info()
    return render_template('empty.html'),202

@application.route('/203')
def return_203():
    print_request_info()
    return render_template('empty.html'),203

@application.route('/204')
def return_204():
    print_request_info()
    return render_template('empty.html'),204

@application.route('/205')
def return_205():
    print_request_info()
    return render_template('empty.html'),205

@application.route('/206')
def return_206():
    print_request_info()
    return render_template('empty.html'),206

@application.route('/300')
def return_300():
    print_request_info()
    return render_template('empty.html'),300

@application.route('/301')
def return_301():
    print_request_info()
    return redirect(url_for('return_200'),301)

@application.route('/302')
def return_302():
    print_request_info()
    return redirect(url_for('return_200'),302)

@application.route('/303')
def return_303():
    print_request_info()
    return redirect(url_for('return_200'),303)

@application.route('/304')
def return_304():
    print_request_info()
    return render_template('empty.html'),304

@application.route('/305')
def return_305():
    print_request_info()
    return redirect(url_for('return_200'),305)

@application.route('/307')
def return_307():
    print_request_info()
    return redirect(url_for('return_200'),307)

@application.route('/308')
def return_308():
    print_request_info()
    return redirect(url_for('return_200'),308)

@application.route('/400')
def return_400():
    print_request_info()
    abort(400)

@application.route('/401')
def return_401():
    print_request_info()
    abort(401)

@application.route('/402')
def return_402():
    print_request_info()
    abort(402)

@application.route('/403')
def return_403():
    print_request_info()
    abort(403)

@application.route('/404')
def return_404():
    print_request_info()
    abort(404)

@application.route('/405')
def return_405():
    print_request_info()
    abort(405)

@application.route('/406')
def return_406():
    print_request_info()
    abort(406)

@application.route('/407')
def return_407():
    print_request_info()
    abort(407)

@application.route('/408')
def return_408():
    print_request_info()
    abort(408)

@application.route('/409')
def return_409():
    print_request_info()
    abort(409)

@application.route('/410')
def return_410():
    print_request_info()
    abort(410)

@application.route('/411')
def return_411():
    print_request_info()
    abort(411) 

@application.route('/412')
def return_412():
    print_request_info()
    abort(412)

@application.route('/413')
def return_413():
    print_request_info()
    abort(413)

@application.route('/414')
def return_414():
    print_request_info()
    abort(414)

@application.route('/415')
def return_415():
    print_request_info()
    abort(415)

@application.route('/500')
def return_500():
    print_request_info()
    abort(500)

@application.route('/501')
def return_501():
    print_request_info()
    abort(501)

@application.route('/502')
def return_502():
    print_request_info()
    abort(502)

@application.route('/503')
def return_503():
    print_request_info()
    abort(503)

@application.route('/504')
def return_504():
    print_request_info()
    abort(504)

@application.route('/505')
def return_505():
    print_request_info()
    abort(505)

@application.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404

def print_request_info():
    #request.form, request.args,request.cookies,request.headers,request.files,request.method
    print(request.headers)

if __name__ == '__main__':
    application.run(host='0.0.0.0')

