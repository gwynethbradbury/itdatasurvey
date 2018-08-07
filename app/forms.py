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
    alt_email = fields.StringField('Please give an alternative contact email which we can use to contact you if/when you leave the University:')#, validators=[DataRequired()])
    # Supply Media
    supply_media = fields.SelectMultipleField('Media types in which the data resource can be supplied (select all that apply):',
                                              choices=[("spreadsheets","Spreadsheets"),
                                                       ("images","Images"),
                                                       ("video","Video"),
                                                       ("audio","Audio"),
                                                       ("surveys","Surveys"),
                                                       ("text","Text")])
    # File Size(estimate)
    file_size_estimate = fields.StringField('The estimated current total size of the data asset (e.g. 10GB)')
    # num records held
    num_records = fields.SelectField('Choose the approximate number of records (number of persons) holding personal data:',
                                        choices=[('<1k','< 1,000'),
                                                 ('1k-5k','1,000 - 5,000'),
                                                 ('5k-10k','5,000-10,000'),
                                                 ('>10k','> 10,000')])
    # File Size(final)
    file_size_final = fields.StringField('The estimated predicted total size of the final data asset (e.g. 1TB)')


    asset_name = fields.StringField("Please give the name of this data set. If you are filling this form out for multiple sets of data at once, please either give a generic name for the data you hold, or separate explicit names with commas.")
    linux_or_windows = fields.RadioField("Please select storage location:",
        choices=[('linux', 'Linux'), ('windows', 'Windows')],default='linux')
    shared_or_personal = fields.RadioField("Is this data stored in your home drive, or in a shared project or resource space?",
        choices=[('shared', 'Shared'), ('home', 'My home drive')], default='home')
    path = fields.StringField("Please enter the path to the data on SoGE servers.")


    from models import administrative_data_type,research_data_type


    # data_type = fields.SelectField("Is this data used for administrative or research purposes?",choices=[("Administrative","Administrative"),("Research","Research")])
    admin_datatype = fields.SelectMultipleField("Select the type of data that you hold:",choices=[(a,a) for a in administrative_data_type])
    research_datatype = fields.SelectMultipleField("Select the type of data that you hold:",choices=[(a,a) for a in research_data_type])
    is_data_personal = fields.RadioField('Is this data personal in nature?', choices=[('Y1', 'Yes'), ('N1', 'No')], default='N1')
    curec_accepted = fields.BooleanField('Did you receive CUREC approval? <a href="https://researchsupport.admin.ox.ac.uk/governance/ethics/apply/sshidrec#collapse394921" class="text-info" target="_blank">Info.</a>')
    curec_date = fields.DateField("If so, select the date that the CUREC form was accepted:")
    data_source = fields.RadioField("Did you collect this data yourself?",choices=[("me","Yes, I did"),("other","No")],default='me')
    license_or_data_source = fields.TextAreaField("Please enter the license text or a description of the data source for this data")

from models import KnownThirdPartySupplier, information_types2,information_typesx, data_classes2
class ThirdPartySurvey(Form):
    # Alternative Email
    alt_email = fields.StringField('Please give an alternative contact email',validators=[fields.validators.Optional()])  # , validators=[DataRequired()])


    uses_third_parties = fields.RadioField("Do you use any third party service providers to store and/or process research data?",
                                           choices=[('Y','Yes'),('N','No')], default='Y',validators=[fields.validators.Optional()])

    supplier_list = fields.SelectMultipleField("Select all suppliers that you use",
                                          choices=[(a,a) for a in KnownThirdPartySupplier.get_all_names()],validators=[fields.validators.Optional()])

    description = fields.TextAreaField("Please describe how you use this service. If you have selected 'Other' from the list, please name any unlisted services:",validators=[fields.validators.Optional()])
    information_type = fields.SelectMultipleField("Please select the Information type stored with this service:",
                                          choices=[(information_types2[i],information_types2[i]) for i in range(len(information_typesx))],validators=[fields.validators.Optional()])

    division = fields.SelectField("Select the division that uses this data:",
                                  choices=[("social_sci","Social Sciences"), ("humanities","Humanities")],validators=[fields.validators.Optional()])

    data_classification = fields.SelectField("Select the privacy classification for this data:",choices=[(a,a) for a in data_classes2],validators=[fields.validators.Optional()])  # Data Classification (see www.infosec.ox.ac.uk)
    data_volume_records = fields.SelectField("Select the number of personal records stored in this service:",
                                             choices=[("<1000","<1000"), ("1000-4999","1000-4999"), ("5000-10k","5000-10k"), (">10k",">10k")],validators=[fields.validators.Optional()])  # Data Volume
    data_compliance = fields.SelectField("Select the type of data compliance required for this service:",
                                         choices=[("Unspecific","Unspecific"), ("Specific","Specific")],validators=[fields.validators.Optional()])
#

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

    linux_or_windows = fields.RadioField("If 'other' selected, please select storage type",
        choices=[('linux', 'Linux'), ('windows', 'Windows')])

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

class Survey3Form(Form):

    has_site= fields.RadioField("Do you maintain or administer any websites related to your, or your group's, research?",
        choices=[('Y', 'Yes'), ('N', 'No')],
        # validators=[DataRequired()], default=None
                                 )

    other_site = fields.StringField("If 'other' selected, please enter site name")
    url = fields.StringField("What is the URL used to access this site?")

    hosted_by_soge = fields.RadioField("Is this site hosted internally on SoGE infrastucture, or on an external server?",
        choices=[('I', 'Internal'), ('E', 'External')])

    explanation = fields.TextAreaField('What is the motivation for hosting your site externally to SoGE? (e.g. collaboration with external parteners, computation, storage)')

    # Alternative Email
    alt_email = fields.StringField('Please give an alternative contact email')  # , validators=[DataRequired()])




class ConfirmACLForm(Form):

    is_acl_correct = fields.RadioField('Is this list of users correct?',
        choices=[('Y', 'Yes'), ('N', 'No'), ('O', 'Not sure')])

