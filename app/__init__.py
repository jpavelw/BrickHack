__author__ = 'codnee'

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.mail import Mail
from config import HerokuConfig

app = Flask(__name__)
app.config.from_object(HerokuConfig)

db = SQLAlchemy(app)
mail = Mail(app)

cache = None

import users
from flask.ext.security import login_required, current_user
from flask import request, render_template, send_from_directory


@app.route('/')
@login_required
def hello_world():
    return "Meh"

@app.route('/img/<file>')
@app.route('/css/<file>')
@app.route('/js/<file>')
def send_js(file):
    return send_from_directory('static/' +
        request.path[:4] if request.path[4] is not '/' else request.path[:3], file)

@app.before_first_request
def init_db():
    db.create_all()


@app.before_request
def before():
    if cache and not request.form and not current_user:
        resp = cache.get("%s : %s" % (request.path, request.args.__str__() if len(request.args) > 0 else ""))
        if resp:
            resp.headers["x-from-cache"] = "Oh yeah!"
            resp.cache_control.max_age = 300
            return resp

@app.after_request
def after(resp):
    if "x-from-cache" not in resp.headers:
        resp.headers["x-from-cache"] = "Noup"
        if cache:
            cache.add("%s : %s" % (request.path, request.args.__str__() if len(request.args) > 0 else ""), resp)

    return resp
