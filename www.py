#!/usr/bin/env python3

from flask import Flask,redirect,url_for
from flask_bootstrap import Bootstrap
import sys,os
from flask_wtf.csrf import CSRFProtect
from flask_sqlalchemy_session import flask_scoped_session
from importlib import import_module as im

app = Flask(__name__, static_url_path='/static')

app.config['TEMPLATES_AUTO_RELOAD']=True

bps = "root"

for bp in bps.split():
    m = im("views." + bp)
    app.register_blueprint(m.bp)

Bootstrap(app)

if __name__ == "__main__":
    print("Running MAIN!!!")
    app.run( host='127.0.0.1', port=8800, threaded=True )




