# -*- coding: utf-8 -*-

import os
from datetime import timedelta

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail
#from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.config.from_object('config')



db = SQLAlchemy(app)


lm = LoginManager()
lm.init_app(app)
lm.login_view = 'login'

mail = Mail(app)

#csrf = CSRFProtect(app)

app.secret_key = os.urandom(24)
app.permanent_session_lifetime = timedelta(minutes=120)

groups=['15_20deg_water_resources',
        'arve',
        'beta-diversity',
        'carina',
        'clarify',
        'ComputationalScience',
        'do4models',
        'EcosystemsLab_TLS',
        'enso_flavours',
        'fennec',
        'gem',
        'ghm',
        'gwava',
        'hiasa',
        'impala',
        'leaf-gpu',
        'leap',
        'marius',
        'mistral',
        'mooredrought',
        'okvbasin_sdm',
        'pollcurb',
        'reach',
        'river-routing',
        'seviri_dust',
        'sfp-datascience',
        'soge_routines',
        'titan',
        'tnc',
        'umfula',
        'weather_attribution']

import views
import models
