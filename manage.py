# -*- coding: utf-8 -*-

from flask_script import Manager
from app import app, db

from app.models import InformationAssetInventory as PersonalSurvey,SharedSurvey,\
    SharedSpace,Website,ThirdPartyRegister,KnownThirdPartySupplier

from flask_migrate import Migrate, MigrateCommand
import os
# ALEMBIC
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_option('-c', '--config', dest='config', required=False)





@manager.command
def write_output():
    from app.models import InformationAssetInventory, ThirdPartyRegister
    InformationAssetInventory.produce_out_file(os.path.join(app.config['OUTPUT_FOLDER'], 'InformationAssetInventory.csv'))
    ThirdPartyRegister.produce_out_file(os.path.join(app.config['OUTPUT_FOLDER'], 'ThirdPartyRegister.csv'))


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
               ]
               # ('Other', 'cenv0594')]

    sites = [('Other', 'cenv0594')]
    #infrastructure","platform","software","cots","custom_software","outsourced_service_provider","other
    #    data_location = db.Column(db.Enum("UK", "EEA", "non-EEA"))# Data Location

    tps=[("Other","other"),
         ("Dropbox","other"),
         ("Amazon Web Service (AWS)","platform",)]

    for f in folders:
        s = SharedSpace(f[1],f[0],'linux')
        db.session.add(s)
    for s in sites:
        ss = Website(s[1],s[0])
        db.session.add(ss)
    for s in tps:
        ss = KnownThirdPartySupplier(s[0],"",s[1],"","non-EEA")
        db.session.add(ss)

    db.session.commit()



# if __name__ == "__main__":
#     app.run(port=5006)





manager.add_command('db', MigrateCommand)
if __name__ == '__main__':
    # initdb()
    manager.run()


# initialise:
# python manage.py db init

# migrate/update:
# python manage.py db migrate

# apply update:
# python manage.py db upgrade
