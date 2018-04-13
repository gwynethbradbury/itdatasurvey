# -*- coding: utf-8 -*-

from flask_wtf import Form, fields#, validators, DataRequired, Email, Regexp
import wtforms as fields
from app import db


# def validate_login(form, field):
#     user = form.get_user()
#     if user is None:
#         raise validators.ValidationError('Invalid user')
#     if user.password != form.password.data:
#         raise validators.ValidationError('Invalid password')
#
#
# class LoginForm(Form):
#     email = fields.TextField(validators=[Required(), Email()])
#     password = fields.PasswordField(validators=[Required(), validate_login])
#
#     def get_user(self):
#         return db.session.query(User).filter_by(email=self.email.data).first()
#
#
# class ForgotPasswordForm(Form):
#     email = fields.TextField(validators=[Required(), Email()])
#
#     def get_user(self):
#         return db.session.query(User).filter_by(email=self.email.data).first()
#
#
# class RegistrationForm(Form):
#     email = fields.TextField('Email Address',
#         validators=[Required(), Email(), Regexp('[^@]+@[^@]+[fsu]+\.[edu]+')])
#     consent = fields.BooleanField(validators=[Required()])
#     password = fields.PasswordField('New Password', [
#         validators.Required(), validators.Length(min=8, max=20),
#         validators.EqualTo('confirm', message='Passwords must match')
#     ])
#     confirm = fields.PasswordField(validators=[Required()])
#
#     def validate_email(self, field):
#         if db.session.query(User).filter_by(email=self.email.data).count() > 0:
#             raise validators.ValidationError('Duplicate email')
#
#
# class NewPass(Form):
#     password = fields.PasswordField('New Password', [
#         validators.DataRequired(), validators.Length(min=8, max=20),
#         validators.EqualTo('confirm', message='Passwords must match')
#     ])
#     confirm = fields.PasswordField(validators=[DataRequired()])


class Survey1Form(Form):

    has_data = fields.RadioField('Do you store personal data on SoGE IT infrastructure?',
        choices=[('Y', 'Yes'), ('N', 'No')],
        # validators=[DataRequired()], default=None
                                 )

    # Alternative Email
    alt_email = fields.StringField('Please give an alternative contact email')#, validators=[DataRequired()])
    # Supply Media
    supply_media = fields.StringField('Media formats in which the data resource can be supplied')
    # File Size(estimate)
    file_size_estimate = fields.StringField('The estimated size of the files')
    # File Size(final)
    file_size_final = fields.StringField('The final size of the files')
    # Format Name
    format_name = fields.StringField('Data resource format type (examples: images, video, text)')
    # Use Constraints
    use_constraints = fields.TextAreaField('Description of the restrictions and legal prerequisites for accessing and using the data resource. <br/>'
                                           'Describe the conditions which must be accepted to access and use the data. Adress conditions such as the protection of privacy, '
                                           'security of intellectual property (IP) rights, copyright issues,'
                                           'and any other restrictions and limitations established as terms for data access and use.')
    # Limitations on Public Access
    public_access_constraints = fields.TextAreaField('Description of the restrictions and legal prerequisites for accessing the data resource. <br/>'
                                           'Describe the conditions which must be accepted to access the data. Adress conditions such as the protection of privacy, '
                                           'security of intellectual property (IP) rights, copyright issues,'
                                           'and any other restrictions and limitations established as terms for data access.')
    # Process Status
    process_status = fields.SelectField('Current status of the data creation process:',
                                        choices=[('1','1. Completed - Production of the data has been completed'),
                                                 ('2','2. Historical Archive - Data has been backed up in an offline storage facility'),
                                                 ('3','3. Obsolete - Data is nolonger relevant'),
                                                 ('4','4. Ongoing - Data is continually being updated'),
                                                 ('5','5. Planned - Fixed data for data collection or compleion has been established')])
    # Description of Process Steps
    process_steps_description = fields.TextAreaField('A general description of how the data was obtained.<br/>'
                                                     'Provide details of the steps taken to construct the dataset and the processes used to process the data.'
                                                     'This descriptive history of the data is useful in determining its fitness-for-use for particular applications and analyses.'
                                                     'The description should include the hardware and software used and an scanning or digitisation steps'
                                                     'as well as any methods of processing the data, such as anonymisation of personal details of participants.')
    # Lineage
    lineage = fields.TextAreaField('Information about the source data used in the construction of the dataset<br/>'
                                   'Lineage information can represent a list of feature and attribute sources compiled to create the data resource.'
                                   'These sources can include photography, images, videography, and people involved in data collection.<br/>'
                                   'It is recognised that this may not have been documented when the resource was created. '
                                   'Any data sources involving human participants should have been subject to CUREC requirements. CUREC forms may be attached at the end of the survey.')
    # Experimental design / sampling regime
    experimental_design = fields.TextAreaField('Experimental Design: indicate if such information is available, either by entering ublished document information (DOI) or details directly into the field.')
    # Collection / generation / transformation methods
    collection_generation_transformation_methods = fields.TextAreaField('Collection, Generation and Transformation Methods: '
                                                                        'indicate if such information is available, either by entering ublished document information (DOI) or details directly into the field.')
    # Fieldwork and / or laboratory instrumentation
    fieldwork_lab_instrumentation = fields.TextAreaField('Fieldwork or Laboratory Instrumentation Details: '
                                                         'indicate if such information is available, either by entering ublished document information (DOI) or details directly into the field.')
    # Analytical methods
    analytical_methods = fields.TextAreaField('Analytical Methods: '
                                                         'indicate if such information is available, either by entering ublished document information (DOI) or details directly into the field.')

    # Comments
    comments = fields.TextAreaField('Any further comments:')


class Survey2Form(Form):

    has_data = fields.RadioField('Do you store personal data on SoGE IT infrastructure?',
        choices=[('Y', 'Yes'), ('N', 'No')],
        # validators=[DataRequired()], default=None
                                 )

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
    other_group = fields.StringField("If 'other' selected, please enter group/folder name")


    # Alternative Email
    alt_email = fields.StringField('Please give an alternative contact email')  # , validators=[DataRequired()])
    # Supply Media
    supply_media = fields.StringField('Media formats in which the data resource can be supplied')
    # File Size(estimate)
    file_size_estimate = fields.StringField('The estimated size of the files')
    # File Size(final)
    file_size_final = fields.StringField('The final size of the files')
    # Format Name
    format_name = fields.StringField('Data resource format type (examples: images, video, text)')
    # Use Constraints
    use_constraints = fields.TextAreaField(
        'Description of the restrictions and legal prerequisites for accessing and using the data resource. <br/>'
        'Describe the conditions which must be accepted to access and use the data. Adress conditions such as the protection of privacy, '
        'security of intellectual property (IP) rights, copyright issues,'
        'and any other restrictions and limitations established as terms for data access and use.')
    # Limitations on Public Access
    public_access_constraints = fields.TextAreaField(
        'Description of the restrictions and legal prerequisites for accessing the data resource. <br/>'
        'Describe the conditions which must be accepted to access the data. Adress conditions such as the protection of privacy, '
        'security of intellectual property (IP) rights, copyright issues,'
        'and any other restrictions and limitations established as terms for data access.')
    # Process Status
    process_status = fields.SelectField('Current status of the data creation process:',
                                        choices=[('1', '1. Completed - Production of the data has been completed'),
                                                 ('2',
                                                  '2. Historical Archive - Data has been backed up in an offline storage facility'),
                                                 ('3', '3. Obsolete - Data is nolonger relevant'),
                                                 ('4', '4. Ongoing - Data is continually being updated'),
                                                 ('5',
                                                  '5. Planned - Fixed data for data collection or compleion has been established')])
    # Description of Process Steps
    process_steps_description = fields.TextAreaField('A general description of how the data was obtained.<br/>'
                                                     'Provide details of the steps taken to construct the dataset and the processes used to process the data.'
                                                     'This descriptive history of the data is useful in determining its fitness-for-use for particular applications and analyses.'
                                                     'The description should include the hardware and software used and an scanning or digitisation steps'
                                                     'as well as any methods of processing the data, such as anonymisation of personal details of participants.')
    # Lineage
    lineage = fields.TextAreaField('Information about the source data used in the construction of the dataset<br/>'
                                   'Lineage information can represent a list of feature and attribute sources compiled to create the data resource.'
                                   'These sources can include photography, images, videography, and people involved in data collection.<br/>'
                                   'It is recognised that this may not have been documented when the resource was created. '
                                   'Any data sources involving human participants should have been subject to CUREC requirements. CUREC forms may be attached at the end of the survey.')
    # Experimental design / sampling regime
    experimental_design = fields.TextAreaField(
        'Experimental Design: indicate if such information is available, either by entering ublished document information (DOI) or details directly into the field.')
    # Collection / generation / transformation methods
    collection_generation_transformation_methods = fields.TextAreaField(
        'Collection, Generation and Transformation Methods: '
        'indicate if such information is available, either by entering ublished document information (DOI) or details directly into the field.')
    # Fieldwork and / or laboratory instrumentation
    fieldwork_lab_instrumentation = fields.TextAreaField('Fieldwork or Laboratory Instrumentation Details: '
                                                         'indicate if such information is available, either by entering ublished document information (DOI) or details directly into the field.')
    # Analytical methods
    analytical_methods = fields.TextAreaField('Analytical Methods: '
                                              'indicate if such information is available, either by entering ublished document information (DOI) or details directly into the field.')

    # Comments
    comments = fields.TextAreaField('Any further comments:')

class ConfirmACLForm(Form):

    is_acl_correct = fields.RadioField('Is this list of users correct?',
        choices=[('Y', 'Yes'), ('N', 'No'), ('O', 'Not sure')])

