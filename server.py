from flask import Flask
from flask import render_template, abort, make_response, redirect, url_for
from flask import request, Response
from routes import routes

from logging import DEBUG

application = Flask(__name__)
application.logger.setLevel(DEBUG)
routes.define_routes(application)

if __name__ == '__main__':
    application.run(host='0.0.0.0')

