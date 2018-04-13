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

    folders = [('15_20deg_water_resources', 'cenv0594'),
               ('arve', 'cenv0594'),
               ('beta-diversity', 'cenv0594'),
               ('carina', 'cenv0594'),
               ('clarify', 'cenv0594'),
               ('ComputationalScience', 'cenv0594'),
               ('do4models', 'cenv0594'),
               ('EcosystemsLab_TLS', 'cenv0594'),
               ('enso_flavours', 'cenv0594'),
               ('fennec', 'cenv0594'),
               ('gem', 'cenv0594'),
               ('ghm', 'cenv0594'),
               ('gwava', 'cenv0594'),
               ('hiasa', 'cenv0594'),
               ('impala', 'cenv0594'),
               ('leaf-gpu', 'cenv0594'),
               ('leap', 'cenv0594'),
               ('marius', 'cenv0594'),
               ('mistral', 'cenv0594'),
               ('mooredrought', 'cenv0594'),
               ('okvbasin_sdm', 'cenv0594'),
               ('pollcurb', 'cenv0594'),
               ('reach', 'cenv0594'),
               ('river-routing', 'cenv0594'),
               ('seviri_dust', 'cenv0594'),
               ('sfp-datascience', 'cenv0594'),
               ('soge_routines', 'cenv0594'),
               ('titan', 'cenv0594'),
               ('tnc', 'cenv0594'),
               ('umfula', 'cenv0594'),
               ('weather_attribution', 'cenv0594'),
               ('Other', 'cenv0594')]
    for f in folders:
        s = SharedSpace(f[1],f[0],'linux')
        db.session.add(s)

    db.session.commit()

if __name__ == "__main__":
    # initdb()
    app.run(port=5000)
