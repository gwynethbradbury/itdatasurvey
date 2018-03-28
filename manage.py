# -*- coding: utf-8 -*-

from flask.ext.script import Manager
from app import app, db

from app.models import User, PersonalSurvey,SharedSurvey

manager = Manager(app)
manager.add_option('-c', '--config', dest='config', required=False)


@manager.command
def initdb():
    """initialize database"""
    db.drop_all()
    db.create_all()

    admin = User(
        email=u'admin@yourdomain.com',
        password=u'unconquered',
        role=1)
    db.session.add(admin)
    db.session.commit()

if __name__ == "__main__":
    app.run(port=3000)
