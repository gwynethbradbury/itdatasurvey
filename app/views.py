# -*- coding: utf-8 -*-

from flask import render_template, flash, redirect
from flask import url_for, g, request

from flask.ext.login import login_user, logout_user, current_user, login_required
from flask.ext.sqlalchemy import get_debug_queries

from models import PersonalSurvey as Survey1, SharedSurvey as Survey2, SharedSpace, WebhostingSurvey as Survey3, Website
from forms import Survey1Form, Survey2Form, Survey3Form, ConfirmACLForm
from email import user_notification, forgot_password
from config import DATABASE_QUERY_TIMEOUT
from app import app, db, lm
from decorators import admin_required

from datetime import date
import uuid
import datetime

import wtforms as fields


from auth.iaasldap import LDAPUser as LDAPUser

current_user = LDAPUser()


@app.context_processor
def inject_paths():
    return dict(LDAPUser=current_user)

@app.route('/survey_1/', methods=['GET', 'POST'])
# @login_required
def survey_1():
    if not Survey1.has_been_done_by(current_user.uid_trim(),datetime.datetime.utcnow().year)[0]:
        form = Survey1Form(request.form)

        if form.validate_on_submit():
            survey = Survey1(current_user.uid_trim(),alt_email="not a real email")
            form.populate_obj(survey)
            db.session.add(survey)

            db.session.commit()
            return redirect(url_for('index'))
        elif request.form.get('has_data')=='N':
            survey = Survey1(current_user.uid_trim(), alt_email="none required")
            db.session.add(survey)

            db.session.commit()
            return redirect(url_for('index'))

        return render_template('survey/Survey1.html', title='Survey', form=form)
    else:
        return redirect(url_for('index'))


@app.route('/survey_2/', methods=['GET', 'POST'])
# @login_required
def survey_2():
    g.user = current_user

    # get folders for which this user is a member
    # todo: and for which a survey has not been done this year
    folders = SharedSpace.query.filter_by(PI_username=current_user.uid_trim()).all()
    choices=[]
    for f in folders:
        found=1
        for s in f.surveys.all():
            if s.year == datetime.datetime.utcnow().year:
                found=0 #so dont include this one
                break
        if found:
            choices.append(f.folder_name)
    choices.append('Other')


    # # groups
    # group = fields.SelectField('Group name',
    #                             choices=[('15_20deg_water_resources','15_20deg_water_resources'),
    #                                      ('arve','arve'),
    #                                      ('beta-diversity','beta-diversity'),
    #                                      ('carina','carina'),
    #                                      ('clarify','clarify'),
    #                                      ('ComputationalScience','ComputationalScience'),
    #                                      ('do4models','do4models'),
    #                                      ('EcosystemsLab_TLS','EcosystemsLab_TLS'),
    #                                      ('enso_flavours','enso_flavours'),
    #                                      ('fennec','fennec'),
    #                                      ('gem','gem'),
    #                                      ('ghm','ghm'),
    #                                      ('gwava','gwava'),
    #                                      ('hiasa','hiasa'),
    #                                      ('impala','impala'),
    #                                      ('leaf-gpu','leaf-gpu'),
    #                                      ('leap','leap'),
    #                                      ('marius','marius'),
    #                                      ('mistral','mistral'),
    #                                      ('mooredrought','mooredrought'),
    #                                      ('okvbasin_sdm','okvbasin_sdm'),
    #                                      ('pollcurb','pollcurb'),
    #                                      ('reach','reach'),
    #                                      ('river-routing','river-routing'),
    #                                      ('seviri_dust','seviri_dust'),
    #                                      ('sfp-datascience','sfp-datascience'),
    #                                      ('soge_routines','soge_routines'),
    #                                      ('titan','titan'),
    #                                      ('tnc','tnc'),
    #                                      ('umfula','umfula'),
    #                                      ('weather_attribution','weather_attribution'),
    #                                      ('Other','Other')])


    # survey2 can be done a number of times
    if Survey1.has_been_done_by(current_user.uid_trim(),datetime.datetime.utcnow().year)[0]:#  \
            # and not Survey2.has_been_done_by(current_user.uid_trim(),datetime.datetime.utcnow().year)[0] :

        form = Survey2Form(request.form)

        if form.validate_on_submit():
            survey = Survey2(current_user.uid_trim(),alt_email="not a real email")
            form.populate_obj(survey)
            survey.group = request.form.get('group_name')

            if SharedSpace.query.filter_by(folder_name=request.form.get('group_name')).count()==0:
                sharedspace = SharedSpace(current_user.uid_trim(),request.form.get('other_group'),request.form.get('linux_or_windows'))
                db.session.add(sharedspace)
                db.session.commit()
            else:
                sharedspace = SharedSpace.query.filter_by(folder_name=request.form.get('group_name')).first()
            survey.shared_space_id = sharedspace.id
            db.session.add(survey)

            db.session.commit()

            return redirect(url_for('confirm_ACL',sharedspace_id=sharedspace.id))
        elif request.form.get('has_data')=='N':
            survey = Survey2(current_user.uid_trim(), alt_email="none required")
            db.session.add(survey)

            db.session.commit()
            return redirect(url_for('index'))

        return render_template('survey/Survey2.html', title='Survey', form=form,groupfield=choices)
    else:
        return redirect(url_for('index'))


@app.route('/survey_3/', methods=['GET', 'POST'])
# @login_required
def survey_3():
    g.user = current_user

    # get folders for which this user is a member
    # todo: and for which a survey has not been done this year
    sites = Website.query.filter_by(PI_username=current_user.uid_trim()).all()
    choices=[]
    for f in sites:
        found=1
        for s in f.surveys.all():
            if s.year == datetime.datetime.utcnow().year:
                found=0 #so dont include this one
                break
        if found:
            choices.append(f.site_name)
    choices.append('Other')

    if Survey1.has_been_done_by(current_user.uid_trim(),datetime.datetime.utcnow().year)[0] \
            and Survey2.has_been_done_by(current_user.uid_trim(),datetime.datetime.utcnow().year)[0]:

        form = Survey3Form(request.form)

        if form.validate_on_submit():
            survey = Survey3(current_user.uid_trim(),alt_email="not a real email")
            form.populate_obj(survey)
            survey.site = request.form.get('site_name')
            if Website.query.filter_by(site_name=request.form.get('site_name')).count()==0:
                website = Website(current_user.uid_trim(),request.form.get('other_site'),request.form.get('url'))
                db.session.add(website)
                db.session.commit()
            else:
                website = Website.query.filter_by(site_name=request.form.get('site_name')).first()
            survey.website_id = website.id
            db.session.add(survey)

            db.session.commit()
            return redirect(url_for('index'))
        elif request.form.get('has_site')=='N':
            survey = Survey3(current_user.uid_trim(), alt_email="none required")
            db.session.add(survey)

            db.session.commit()
            return redirect(url_for('index'))

        return render_template('survey/Survey3.html', title='Survey', form=form,sitefield=choices)
    else:
        return redirect(url_for('index'))

@app.route('/confirm_acl/<sharedspace_id>', methods=['GET', 'POST'])
def confirm_ACL(sharedspace_id):

    ss = SharedSpace.query.get_or_404(sharedspace_id)
    if not ss.PI_username == current_user.uid_trim():
        flash("you are not authorised for this shared space",category="error")
        return redirect(url_for('index'))

    if ss.storage_type=='linux':
        users = getMembersOfLDAPGroup()
    else:
        users = getMembersOfWinroup()

    users=[current_user]
    # if users.__len__()>0:
    #     return render_template('survey/confirm_acl.html', users=users)

    form=ConfirmACLForm(request.form)

    # if form.validate_on_submit():
    if request.method == 'POST':
        A = request.form.get('is_acl_correct')
        if A == 'Y':
            ss.is_acl_correct=1
        elif A =='N':
            ss.is_acl_correct=0
        else:
            ss.is_acl_correct=None

        db.session.add(ss)
        db.session.commit()


        return redirect(url_for('index'))

    return render_template('survey/confirm_acl.html', title='Survey', form=form, users=users, sharedspace=ss)



# todo: get list of members
def getMembersOfLDAPGroup():
    pass
def getMembersOfWinroup():
    pass



@app.route('/information')
def information():
    return render_template("info.html")

@app.route('/')
@app.route('/index')
# @login_required
def index():
    user = current_user
    # if user.has_role('superusers'):
    #     return redirect('admin/')
    survey1_done,survey1_details = Survey1.has_been_done_by(current_user.uid_trim(),datetime.datetime.utcnow().year)
    survey2_done,survey2_details = Survey2.has_been_done_by(current_user.uid_trim(),datetime.datetime.utcnow().year)
    survey3_done,survey3_details = Survey3.has_been_done_by(current_user.uid_trim(),datetime.datetime.utcnow().year)
    return render_template("index.html", title="Home", user=user,
                           s1=survey1_done,
                           s1_year=datetime.datetime.utcnow().year,
                           s2=survey2_done,
                           s2_details = survey2_details,
                           s3=survey3_done,
                           s3_details = survey3_details)




@app.before_request
def before_request():
    g.user = current_user


@app.errorhandler(404)
def internal_error(error):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500


@app.after_request
def after_request(response):
    for query in get_debug_queries():
        if query.duration >= DATABASE_QUERY_TIMEOUT:
            app.logger.warning("SLOW QUERY: %s\nParameters: %s\nDuration: %fs\nContext: %s\n" %
                (query.statement, query.parameters, query.duration, query.context))
    return response


def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text, error))


# @app.route('/admin')
# # @login_required
# # @admin_required
# def admin():
#     users = []#User.query.filter_by(role=0)
#     return render_template('admin/index.html', title="Admin", users=users)


# @app.route('/admin_survey1/')
# # @login_required
# # @admin_required
# def admin_survey1():
#     surveys = Survey1.query.all()
#     return render_template('admin/partials/survey1.html', title='Admin Personal Survey', surveys=surveys)
#
#
# @app.route('/admin_survey2/')
# # @login_required
# # @admin_required
# def admin_survey2():
#     surveys = Survey2.query.all()
#     return render_template('admin/partials/survey2.html', title='Admin Shared Survey', surveys=surveys)
#
#
# @app.route('/admin_shared_spaces/')
# # @login_required
# # @admin_required
# def admin_shared_spaces():
#     spaces = SharedSpace.query.all()
#     return render_template('admin/partials/shared_spaces.html', title='Admin Shared Spaces', surveys=spaces)




#****************************************
# ADMIN

from flask_admin import Admin, AdminIndexView

from flask_admin.contrib.sqla import ModelView


# Flask and Flask-SQLAlchemy initialization here
# from flask_login import current_user


class MyAdminIndexView(AdminIndexView):
    def is_accessible(self):
        if current_user.has_role('superusers'):
            return True
        return False

    def inaccessible_callback(self, name, **kwargs):
        # redirect to login page if user doesn't have access
        return redirect(url_for('index'))


class MyModelView(ModelView):
    def is_accessible(self):
        if current_user.has_role('superusers'):
            return True
        return False

    def inaccessible_callback(self, name, **kwargs):
        # redirect to login page if user doesn't have access
        return redirect(url_for('index'))




admin = Admin(app, name='ADMIN',
              template_mode='bootstrap3',
              index_view=MyAdminIndexView())

admin.add_view(MyModelView(Survey1, db.session))
admin.add_view(MyModelView(Survey2, db.session))
admin.add_view(MyModelView(SharedSpace, db.session))