# -*- coding: utf-8 -*-

from flask.ext.script import Manager
from app import app, db

from app.models import PersonalSurvey,SharedSurvey,SharedSpace

manager = Manager(app)
manager.add_option('-c', '--config', dest='config', required=False)





@manager.command
def initdb():
    """initialize database"""
    db.drop_all()
    db.create_all()

    folders = ['15_20deg_water_resources',
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
               'weather_attribution',
               'Other']
    for f in folders:
        s = SharedSpace('cenv0594',f,'linux')
        db.session.add(s)

    db.session.commit()

if __name__ == "__main__":
    # initdb()
    app.run(port=5000)
