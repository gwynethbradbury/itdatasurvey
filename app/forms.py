# -*- coding: utf-8 -*-

from flask_wtf import Form, fields#, validators, DataRequired, Email, Regexp
import wtforms as fields
from models import User
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
        choices=[('Y', 'Yes'), ('N', 'No'), ('O', "I don't know")],
        # validators=[DataRequired()], default=None
                                 )

    # gender = fields.RadioField('What is your gender?',
    #     choices=[('M', 'Male'), ('F', 'Female'), ('O', 'I prefer not to answer')],
    #     validators=[Required()], default=None)
    # age = fields.RadioField('What is your age?',
    #     choices=[('lt18', 'Younger than 18'), ('18-24', '18 to 24'), ('25-34', '25 to 34'),
    #         ('35-44', '35 to 44'), ('45-54', '45 to 54'), ('55', '55 years or older')],
    #     validators=[Required()])
    # education = fields.RadioField('Which of the following best describes your highest education level?',
    #     choices=[('Hsg', 'High school graduate'),
    #         ('Scnd', 'Some college, no degree'), ('Assoc', 'Associates Degree'),
    #         ('Bach', 'Bachelors degree'), ('Grad', 'Graduate degree (Masters, Doctorate, etc.)'),
    #         ('O', 'Other')],
    #     validators=[Required()])
    # language = fields.TextField('What is your native language', validators=[Required()])



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
    major = fields.RadioField('Are you majoring in or do you have a degree or job in computer science, computer engineering, information technology, or a related field?',
        choices=[('Y', 'yes'), ('N', 'No'), ('O', 'I prefer not to answer')])#,validators=[DataRequired()])
    count = fields.RadioField('How many website user-names and passwords do you have, approximately?',
        choices=[('lt5', 'Less than 5 accounts'),
            ('5-10', '5 to 10 Accounts'), ('11-20', '11 to 20 Accounts'),
            ('gt20', 'More Than 20 Accounts')])
    unique = fields.RadioField('Do you try to create unique passwords for each different account?',
        choices=[('Y', 'Yes, I create a new password every time I create a new account or every time I have to change my password'),
            ('N', 'No, I use my old passwords that I have already created for my other accounts'),
            ('O', 'I mostly create a new password, but sometimes use old passwords')])#,validators=[DataRequired()])
    department = fields.TextField('In what department are you majoring')#, validators=[DataRequired()])


class Survey3Form(Form):
    choose_names = fields.BooleanField('Names of family members, relatives, close friends')
    choose_numbers = fields.BooleanField('Familiar numbers (birth date, telephone number, street address, employee number, etc.)')
    choose_songs = fields.BooleanField('Songs, movies, television shows, books, poetry or games')
    choose_mnemonic = fields.BooleanField('Scientific or other educational mnemonics')
    choose_sports = fields.BooleanField('Sports teams and players')
    choose_famous = fields.BooleanField('Names of famous people or characters')
    choose_words = fields.BooleanField('Words in a language other than English')
    choose_other = fields.BooleanField('other')
    specify = fields.TextField('please specify')
    secure_numbers = fields.BooleanField('Include numbers')
    secure_upper_case = fields.BooleanField('Include upper case letters')
    secure_symbols = fields.BooleanField('Include symbols(such as "!" or "#")')
    secure_eight_chars = fields.BooleanField('Have 8 or more characters')
    secure_no_dict = fields.BooleanField('Not contain dictionary words')
    secure_adjacent = fields.BooleanField('Not containing a sequence of adjacent or repeated characters on your keyboard (e.g. qwerty)')
    secure_nothing = fields.BooleanField('I did not consider any policy')
    secure_other = fields.BooleanField('other')
    specify1 = fields.TextField('please specify')
    modify = fields.RadioField('Did you create your new password by slightly changing your old password for this website?',
        choices=[('Y', 'Yes'), ('N', 'No')])#,validators=[DataRequired()], default=None)
    usedPassword = fields.RadioField('Is the password that you have just created one that you have used in the past?',
        choices=[('Y', 'Yes'), ('N', 'No'), ('O', 'Password has similarities to another password that I have used before')])#,validators=[DataRequired()], default=None)
    number_N = fields.BooleanField('Not changed')
    number_changed_slightly = fields.BooleanField('Changed Slightly')
    number_changed_completly = fields.BooleanField('Changed Completely')
    number_added_digits = fields.BooleanField('Added Digits')
    number_deleted_digits = fields.BooleanField('Deleted Digits')
    char_N = fields.BooleanField('Not Changed')
    char_changed_slightly = fields.BooleanField('Changed Slightly')
    char_changed_completly = fields.BooleanField('Changed Completly')
    char_added_symbols = fields.BooleanField('Added Symbols')
    char_deleted_symbols = fields.BooleanField('Deleted Symbols')
    not_changed1 = fields.BooleanField('Not changed')
    changed_slightly1 = fields.BooleanField('Changed Slightly')
    changed_completly1 = fields.BooleanField('Changed completely')
    capatalized1 = fields.BooleanField('Capatlized or lower case letters')
    addedwords = fields.BooleanField('Added Words or Letters')
    deletedwords = fields.BooleanField('Deleted Words or Letters')


class Survey4Form(Form):
    computerTime = fields.RadioField('How long have you been using a computer?',
        choices=[('0-2', '0 to 2 Years'), ('3-5', '3 to 5 Years'), ('6-10', '6 to 10 Years'),
            ('mt10', 'More than 10 years')])#,validators=[DataRequired()], default=None)
    pass_random = fields.BooleanField('Randomly generate a password using special software or apps')
    pass_reuse = fields.BooleanField('Reuse a password that is used for another account')
    pass_modify = fields.BooleanField('Modify a password that is used for another account')
    pass_new = fields.BooleanField('Create a new password using a familiar number or a name of a family member')
    pass_substitute = fields.BooleanField('Choose a word and substitute some letters with numbers of symbols (for example @ for a)')
    pass_multiword = fields.BooleanField('Use a pass-phrase consisting of several words')
    pass_phrase = fields.BooleanField('Choose a phrase and use the first letters of each word')
    pass_O = fields.TextAreaField('Other')
    how_regular_file = fields.BooleanField('I store my passwords in a regular file / document on my computer.')
    how_encrypted = fields.BooleanField('I store my passwords in an encrypted computer file')
    how_software = fields.BooleanField('I use password management software to securely store my passwords')
    how_cellphone = fields.BooleanField('I store my passwords on my cellphone / smartphone')
    how_browser = fields.BooleanField('I save my passwords in the browser')
    how_write_down = fields.BooleanField('I write down my password on a piece of paper')
    how_no = fields.BooleanField('No, I do not save my passwords. I remember them.')
    comments = fields.TextAreaField('If you have any additional feedback about passwords or this survey, please enter your comments here.', default=None)