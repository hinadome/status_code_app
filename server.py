from flask import Flask
from flask import render_template, abort, make_response, redirect, url_for
from flask import request, Response
from routes import routes
from logging import DEBUG

application = Flask(__name__)
application.logger.setLevel(DEBUG)
routes.define_routes(application)
application.config['SECRET_KEY'] = '\x97\xdd\xd3\xe6]b?D\xe0VQ\xd5\xff~g\xd2\xf3\x07#\x90\xf6\x1d\xcb\xf6'  

if __name__ == '__main__':
    application.run(host='0.0.0.0')

