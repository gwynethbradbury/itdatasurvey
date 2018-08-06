# -*- coding: utf-8 -*-

from mixins import CRUDMixin
from flask.ext.login import UserMixin

from app import db

import datetime


ROLE_USER = 0
ROLE_ADMIN = 1


# class User(UserMixin, CRUDMixin, db.Model):
#     id = db.Column(db.Integer, primary_key=True, unique=True)
#     userid = db.Column(db.String(255), unique=True)
#     email = db.Column(db.String(255), unique=True)
#     password = db.Column(db.String(20))
#     oldPassword = db.Column(db.String(20))
#     changedPass = db.Column(db.Boolean)
#     role = db.Column(db.SmallInteger, default=ROLE_USER)
#     s1 = db.Column(db.Boolean)
#     s2 = db.Column(db.Boolean)
#     s3 = db.Column(db.Boolean)
#     s4 = db.Column(db.Boolean)
#     lastSeen = db.Column(db.String(255))
#
#     def __init__(
#             self,
#             email=None,
#             userid=None,
#             password=None,
#             oldPassword=None,
#             changedPass=False,
#             s1=False,
#             s2=False,
#             s3=False,
#             s4=False,
#             role=None):
#         self.email = email
#         self.userid = userid
#         self.password = password
#         self.oldPassword = oldPassword
#         self.changedPass = changedPass
#         self.s1 = s1
#         self.s2 = s2
#         self.s3 = s3
#         self.s4 = s4
#         self.role = role
#
#     def is_admin(self):
#         if self.role == 1:
#             return True
#         else:
#             return False
#
#     def is_active(self):
#         return True
#
#     def get_id(self):
#         return unicode(self.id)
#
#     def __repr__(self):
#         return '<User %r>' % (self.email)


administrative_data_type = ["HR/Employment related data - CVs/references/etc",
                            "Financial related data - expenses forms, etc.",
                            "Other Student/staff data (photographs,videos, course lists etc)",
                            "Alumni Data (including Photos",
                            "Other"]
research_data_type = ["Study Datasets",
                      "Other"]
information_types2 = ["HR/Employment related data - CVs/references/etc",
                    "Financial related data - expenses forms, etc.",
                    "Other Student/staff data (photographs,videos, course lists etc)",
                    "Alumni Data (including Photos",
                    "Personal but Non Uni. Members",
                    "Study Datasets",
                    "Other"]

class WebhostingSurvey(db.Model):
    __bind_key__ = 'data_survey'


    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(8), nullable=False)
    date = db.Column(db.Date)
    year = db.Column(db.Integer,nullable=False,default=2018)
    alt_email = db.Column(db.String(100), nullable=False)
    hosted_by_soge = db.Column(db.Enum('I','E'), default='I')
    has_site = db.Column(db.Enum('Y','N'), default='N')

    site = db.Column(db.Enum('first site',
                              'Other'
                              ), nullable=True)
    other_site=db.Column(db.String(20),nullable=True)


    website_id = db.Column(
        db.Integer,
        db.ForeignKey('website.id'),
        nullable=True
    )
    website = db.relationship(
        'Website',
        backref=db.backref(
            'surveys',
            lazy='dynamic'
        )
    )

    def __init__(
            self,
            username, alt_email,
            year=datetime.datetime.utcnow().year):
        self.date = datetime.datetime.utcnow()
        self.year = year
        self.username=username
        self.has_site='N'
        self.site='Other'
        self.alt_email=alt_email


    def get_id(self):
        return unicode(self.id)


    @staticmethod
    def has_been_done_by(username, year=None):

        q= WebhostingSurvey.query.filter(WebhostingSurvey.username==username)
        if year:
            q=q.filter(WebhostingSurvey.year==year)

        if q.count()>0:
            return True,q.all()

        return False,[]


asset_types = db.Enum("Application / System",
                      "Information / data sets (digital)",
                      "Information / data sets (physical)",
                      "Technology (Mobile device - University issued)",
                      "Technology (Mobile device - Personal)",
                      "Technology (Desktop)",
                      "Technology (Server)",
                      "Technology (Network)",
                      "Technology (Telephony)",
                      "Physical (HVAC - Heating, ventilation or air conditioning)",
                      "Physical (Entry system)",
                      "Service provider (Cloud)",
                      "Service provider (IT service)")
data_classes2 = ["Private","Public","Internal"]
data_classes = db.Enum("Private","Public","Internal")
LMH_enum = db.Enum("Low","Medium","High")
times_enum = db.Enum("within 2 hours","within 6 hours","within 24 hours","within 72 hours")


class InformationAssetInventory(db.Model):
    __bind_key__ = 'data_survey'
    __tablename__ = 'information_asset_inventory'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(8), nullable=False)
    date = db.Column(db.Date)
    year = db.Column(db.Integer,nullable=False,default=2018)
    alt_email = db.Column(db.String(100), nullable=False)
    has_assets = db.Column(db.Boolean,default=False)

    asset_type = db.Column(asset_types, default="Information / data sets (digital)")
    asset_name = db.Column(db.String(100), default="Not given")
    asset_owner = db.Column(db.String(100))
    other_details = db.Column(db.Text, default="")
    data_classification = db.Column((data_classes), default="Private")# Data Classification (see www.infosec.ox.ac.uk)
    data_integrity = db.Column(LMH_enum,default="Low")
    data_availability = db.Column(LMH_enum,default="Low")
    recovery_time_objective = db.Column(times_enum,default="within 2 hours")
    recovery_point_objective = db.Column(times_enum,default="within 2 hours")



    supply_media = db.Column(db.String(200), nullable=True, default="Not given")
    file_size_estimate = db.Column(db.String(20), nullable=True, default="Not given")
    file_size_final = db.Column(db.String(20), nullable=True, default="Not given")
    # use_constraints = db.Column(db.Text, nullable=True)
    # public_access_constraints = db.Column(db.Text,nullable=True)
    # process_status = db.Column(
    #     db.Enum(
    #         '1',
    #         '2',
    #         '3',
    #         '4',
    #         '5'
    #     ),
    #     nullable=True
    # )
    # process_steps_description = db.Column(db.Text,nullable=True)
    # lineage = db.Column(db.Text,nullable=True)
    # experimental_design = db.Column(db.Text,nullable=True)
    # collection_generation_transformation_methods = db.Column(db.Text,nullable=True)
    # collection_generation_transformation_methods = db.Column(db.Text,nullable=True)
    # fieldwork_lab_instrumentation = db.Column(db.Text,nullable=True)
    # analytical_methods = db.Column(db.Text,nullable=True)
    # comments = db.Column(db.Text,nullable=True)



    path = db.Column(db.Text, default="")
    data_type = db.Column(db.Enum("Administrative","Research"),default="Administrative")
    data_source = db.Column(db.Enum("me","other"),default="me")
    linux_or_windows = db.Column(db.Enum("linux","windows"),default="linux")
    shared_or_personal = db.Column(db.Enum("home","shared"),default="home")
    # specific_data_type = db.Column(db.String(150),nullable=True)
    is_data_personal = db.Column(db.Boolean,default=False,nullable=False)
    curec_accepted = db.Column(db.Boolean,default=False,nullable=False)
    curec_date = db.Column(db.Date, nullable=True)
    data_source = db.Column(db.Enum("me","other"),nullable=False,default="me")
    license_or_data_source = db.Column(db.Text,nullable=True)

    def __init__(
            self,
            username, alt_email,
            year=datetime.datetime.utcnow().year,asset_owner=None

    ):
        self.date = datetime.datetime.utcnow()
        self.year = year
        self.username=username
        self.has_data=False
        self.alt_email = alt_email
        if asset_owner==None or asset_owner=="":
            self.asset_owner=username
        else:
            self.asset_owner=asset_owner
        self.other_details=""

    def get_id(self):
        return unicode(self.id)

    def get_other_details_field(self):
        #todo: collate fields not in the excel sheet into this field
        pass

    def license_required(self):
        #if the user didn;t collect this data source, they should cite the source and any license agreement
        if self.data_source=="other" and self.data_type=="Research":
            return True
        return False

    def CUREC_required(self):
        # for research data of a personal nature
        if self.data_type=="Research" and self.is_data_personal:
            return True
        return False

    def is_curec_uptodate(self):
        # todo: what is the time limit for CUREC?
        if self.curec_date is not None:
            return True
        return False

    def is_full_survey_required(self):
        # if data is of a personal nature and there is no CUREC form, or it is out of data, or if this is administrative data rather than research
        if self.is_data_personal:
            if not self.is_curec_uptodate():
                return True
            if self.data_type == "Administrative":
                return True
        return False



    @staticmethod
    def has_been_done_by(username, year=None):

        q= InformationAssetInventory.query.filter(InformationAssetInventory.username==username)
        if year:
            q=q.filter(InformationAssetInventory.year==year)

        if q.count()>0:
            return True,q.all()

        return False,[]


    def get_output_for_central_services(self):
        line=""
        if self.has_assets and self.is_data_personal:
            line=str.join(',',[
                str(self.id),
                str(self.asset_type),
                str(self.asset_name),
                str(self.asset_owner),
                str(self.other_details),
                str(self.data_classification),
                str(self.data_integrity),
                str(self.data_availability),
                str(self.recovery_time_objective),
                str(self.recovery_point_objective),
            ]) + "\n"
        return line
    @staticmethod
    def get_headers():
        return "Asset ID," \
               "Asset Type," \
               "Asset Name," \
               "Asset Owner," \
               "Other Asset Information," \
               "Classification / Confidentiality Level," \
               "Integrity," \
               "Availability," \
               "Recovery Time Objective (RTO)," \
               "Recovery Point Objective (RPO)" \
               "\n"
    @staticmethod
    def produce_out_file(filename):
        f = open(filename,'w')
        q = InformationAssetInventory.query.all()
        f.writelines([InformationAssetInventory.get_headers()])
        for a in q:
            f.writelines([a.get_output_for_central_services()])
        f.close()


service_types =db.Enum("infrastructure","platform","software","cots","custom_software","outsourced_service_provider","other")
information_types =db.Enum("financial","hr","student","dev_and_alum","personal_non_uni_members","research","other")
information_typesx =["hr","financial","student","dev_and_alum","personal_non_uni_members","research","other"]

class ThirdPartyRegister(db.Model):
    __bind_key__ = 'data_survey'
    __tablename__ = 'third_party_register'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(8), nullable=False)
    date = db.Column(db.Date)
    year = db.Column(db.Integer,nullable=False,default=2018)
    alt_email = db.Column(db.String(100), nullable=False)
    uses_third_parties = db.Column(db.Enum('Y','N'), default='Y')
    service_user = db.Column(db.String(100))

    Supplier = db.Column(db.Text, default="None",nullable=False)
    # db.Column(db.Integer, db.ForeignKey('known_third_party_supplier.id'), nullable=True)

    description = db.Column(db.String(200),nullable=False)#Description of Service / Usage
    # information_type = db.Column(information_types,default="other")# Information Type
    information_type = db.Column(db.Text,default="other")# Information Type
    division = db.Column(db.Enum("social_sci","humanities"),default="social_sci")# Division
    department = "Geography"# Department / Section
    data_classification = db.Column((data_classes),default="Private")# Data Classification (see www.infosec.ox.ac.uk)
    data_volume_records = db.Column(db.Enum("<1000","1000-4999","5000-10k",">10k"),default="<1000")# Data Volume
    data_compliance = db.Column(db.Enum("Unspecific","Specific"),default="Unspecific")# Data Compliance
    contractual_review = "Adopted supplier's standard  T&Cs.  T&Cs can be changed without notification"# Contractual Review
    assessment = "None/Unknown"# Information Security Team Third Party Security Assessment ouputSupplier

    def __init__(self,
            username, alt_email,
            year=datetime.datetime.utcnow().year,service_user=None):

        self.date = datetime.datetime.utcnow()
        self.year = year
        self.username=username
        self.uses_third_parties='N'
        self.alt_email = alt_email
        if service_user==None or service_user=="":
            self.service_user=username
        else:
            self.service_user=service_user


    def get_id(self):
        return unicode(self.id)

    @staticmethod
    def has_been_done_by(username, year=None):

        q= ThirdPartyRegister.query.filter(ThirdPartyRegister.username==username)
        if year:
            q=q.filter(ThirdPartyRegister.year==year)

        if q.count()>0:
            return True,q.all()

        return False,[]


    def get_output_for_central_services(self):
        line=""
        # if self.has_assets and self.is_data_personal:
        #     line=str.join(',',[
        #         str(self.id),
        #         str(self.asset_type),
        #         str(self.asset_name),
        #         str(self.asset_owner),
        #         str(self.other_details),
        #         str(self.data_classification),
        #         str(self.data_integrity),
        #         str(self.data_availability),
        #         str(self.recovery_time_objective),
        #         str(self.recovery_point_objective),
        #     ]) + "\n"
        return line
    @staticmethod
    def get_headers():
        # return "Asset ID," \
        #        "Asset Type," \
        #        "Asset Name," \
        #        "Asset Owner," \
        #        "Other Asset Information," \
        #        "Classification / Confidentiality Level," \
        #        "Integrity," \
        #        "Availability," \
        #        "Recovery Time Objective (RTO)," \
        #        "Recovery Point Objective (RPO)" \
        #        "\n"
        return ""
    @staticmethod
    def produce_out_file(filename):
        # f = open(filename,'w')
        # q = ThirdPartyRegister.query.all()
        # f.writelines([ThirdPartyRegister.get_headers()])
        # for a in q:
        #     f.writelines([a.get_output_for_central_services()])
        # f.close()
        pass

class KnownThirdPartySupplier(db.Model):
    __bind_key__ = 'data_survey'
    __tablename__ = 'known_third_party_supplier'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60))
    description = db.Column(db.String(100), nullable=False)
    service_type = db.Column((service_types))# Type of Service
    service_owner_email = db.Column(db.String(100))# Service Owner email
    data_location = db.Column(db.Enum("UK", "EEA", "non-EEA"))# Data Location

    @staticmethod
    def get_all_names():
        q = KnownThirdPartySupplier.query.all()
        s=[]
        for a in q:
            s.append(a.name)
        return s

    def __init__(
            self,
            name,description, service_type,service_owner_email,data_location):
        self.name=name
        self.description=description
        self.service_type=service_type
        self.service_owner_email=service_owner_email
        self.data_location=data_location


class SharedSurvey(db.Model):
    __bind_key__ = 'data_survey'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(8), nullable=False)
    date = db.Column(db.Date)
    year = db.Column(db.Integer,nullable=False,default=2018)
    alt_email = db.Column(db.String(100), nullable=False)
    has_data = db.Column(db.Enum('Y','N'), default=True)

    group = db.Column(db.Enum('15_20deg_water_resources',
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
                              'Other'
                              ), nullable=False
        )
    other_group=db.Column(db.String(20),nullable=True)

    shared_space_id = db.Column(
        db.Integer,
        db.ForeignKey('shared_space.id'),
        nullable=True
    )
    shared_space = db.relationship(
        'SharedSpace',
        backref=db.backref(
            'surveys',
            lazy='dynamic'
        )
    )


    supply_media = db.Column(db.String(200), nullable=True)
    file_size_estimate = db.Column(db.String(20), nullable=True)
    file_size_final = db.Column(db.String(20), nullable=True)
    format_name = db.Column(db.String(100), nullable=True)
    use_constraints = db.Column(db.Text, nullable=True)
    public_access_constraints = db.Column(db.Text, nullable=True)
    process_status = db.Column(
        db.Enum(
            '1',
            '2',
            '3',
            '4',
            '5'
        ),
        nullable=True
    )
    process_steps_description = db.Column(db.Text, nullable=True)
    lineage = db.Column(db.Text, nullable=True)
    experimental_design = db.Column(db.Text, nullable=True)
    collection_generation_transformation_methods = db.Column(db.Text, nullable=True)
    collection_generation_transformation_methods = db.Column(db.Text, nullable=True)
    fieldwork_lab_instrumentation = db.Column(db.Text, nullable=True)
    analytical_methods = db.Column(db.Text, nullable=True)
    comments = db.Column(db.Text, nullable=True)


    def __init__(
            self,
            username, alt_email,
            year=datetime.datetime.utcnow().year):
        self.date = datetime.datetime.utcnow()
        self.year = year
        self.username=username
        self.group='Other'
        self.has_data='N'
        self.alt_email=alt_email


    def get_id(self):
        return unicode(self.id)


    @staticmethod
    def has_been_done_by(username, year=None):

        q= SharedSurvey.query.filter(SharedSurvey.username==username)
        if year:
            q=q.filter(SharedSurvey.year==year)

        if q.count()>0:
            return True,q.all()

        return False,[]

class SharedSpace(db.Model):
    __bind_key__ = 'data_survey'

    id = db.Column(db.Integer, primary_key=True)
    PI_username = db.Column(db.String(8), nullable=False)
    folder_name = db.Column(db.String(30), nullable=False)
    storage_type = db.Column(db.Enum('linux','windows'), nullable=True)
    is_acl_correct = db.Column(db.Boolean,nullable=True)

    def most_recent_year(self):
        surveys = SharedSurvey.query.filter_by(shared_space_id=self.id)
        yr=0
        for s in surveys:
            if s.year>yr:
                yr=s.year
        return yr

    def __init__(self,piname,fname,storagetype):
        self.PI_username = piname
        self.folder_name = fname
        self.storage_type = storagetype

    def __str__(self):
        return self.folder_name

class Website(db.Model):
    __bind_key__ = 'data_survey'

    id = db.Column(db.Integer, primary_key=True)
    PI_username = db.Column(db.String(8), nullable=False)
    site_name = db.Column(db.String(100), nullable=False)
    url = db.Column(db.String(100), nullable=False)
    is_soge_hosted = db.Column(db.Enum('Y','N'), default='Y')

    def most_recent_year(self):
        surveys = WebhostingSurvey.query.filter_by(website_id=self.id)
        yr=0
        for s in surveys:
            if s.year>yr:
                yr=s.year
        return yr

    def __init__(self,piname,sname, url="none"):
        self.PI_username = piname
        self.site_name = sname
        self.url = url

    def __str__(self):
        return self.site_name

# class Survey3(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     choose_names = db.Column(db.Boolean)
#     choose_numbers = db.Column(db.Boolean)
#     choose_songs = db.Column(db.Boolean)
#     choose_mnemonic = db.Column(db.Boolean)
#     choose_sports = db.Column(db.Boolean)
#     choose_famous = db.Column(db.Boolean)
#     choose_words = db.Column(db.Boolean)
#     choose_other = db.Column(db.Boolean)
#     specify = db.Column(db.String(255))
#     secure_numbers = db.Column(db.Boolean)
#     secure_upper_case = db.Column(db.Boolean)
#     secure_symbols = db.Column(db.Boolean)
#     secure_eight_chars = db.Column(db.Boolean)
#     secure_no_dict = db.Column(db.Boolean)
#     secure_adjacent = db.Column(db.Boolean)
#     secure_nothing = db.Column(db.Boolean)
#     secure_other = db.Column(db.Boolean)
#     specify1 = db.Column(db.String(255))
#     modify = db.Column(db.String(255))
#     usedPassword = db.Column(db.String(255))
#     number_N = db.Column(db.Boolean)
#     number_changed_slightly = db.Column(db.Boolean)
#     number_changed_completely = db.Column(db.Boolean)
#     number_added_digits = db.Column(db.Boolean)
#     number_deleted_digits = db.Column(db.Boolean)
#     number_substituted_digits = db.Column(db.Boolean)
#     number_O = db.Column(db.String(255))
#     char_N = db.Column(db.Boolean)
#     char_changed_slightly = db.Column(db.Boolean)
#     char_changed_completly = db.Column(db.Boolean)
#     char_added_symbols = db.Column(db.Boolean)
#     char_deleted_symbols = db.Column(db.Boolean)
#     char_substituted_symbols = db.Column(db.Boolean)
#     not_changed1 = db.Column(db.Boolean)
#     changed_slightly1 = db.Column(db.Boolean)
#     changed_completly1 = db.Column(db.Boolean)
#     capatalized1 = db.Column(db.Boolean)
#     addedwords = db.Column(db.Boolean)
#     deletedwords = db.Column(db.Boolean)
#     char_O = db.Column(db.String(255))
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
#     user = db.relationship('User', uselist=False, backref='survey3')
#
#     def __init__(
#             self,
#             choose_names=None,
#             choose_numbers=None,
#             choose_songs=None,
#             choose_mnemonic=None,
#             choose_sports=None,
#             choose_famous=None,
#             choose_words=None,
#             secure_numbers=None,
#             secure_upper_case=None,
#             secure_symbols=None,
#             secure_eight_chars=None,
#             secure_no_dict=None,
#             secure_adjacent=None,
#             secure_nothing=None,
#             modify=None,
#             usedPassword=None,
#             number_N=None,
#             number_added_digits=None,
#             number_deleted_digits=None,
#             number_substituted_digits=None,
#             number_O=None,
#             char_N=None,
#             char_added_symbols=None,
#             char_deleted_symbols=None,
#             char_substituted_symbols=None,
#             char_O=None,
#             userid=None,
#             choose_other=None,
#             specify=None,
#             specify1=None,
#             secure_other=None,
#             number_changed_completly=None,
#             number_changed_slightly=None,
#             char_changed_slightly=None,
#             char_changed_completly=None,
#             not_changed1=None,
#             changed_completly1=None,
#             changed_slightly1=None,
#             capatalized1=None,
#             addedwords=None,
#             deletedwords=None):
#
#         self.choose_names = choose_names
#         self.choose_numbers = choose_numbers
#         self.choose_songs = choose_songs
#         self.choose_mnemonic = choose_mnemonic
#         self.choose_sports = choose_sports
#         self.choose_famous = choose_famous
#         self.choose_words = choose_words
#         self.choose_other = choose_other
#         self.specify = specify
#         self.secure_numbers = secure_numbers
#         self.secure_upper_case = secure_upper_case
#         self.secure_symbols = secure_symbols
#         self.secure_eight_chars = secure_eight_chars
#         self.secure_no_dict = secure_no_dict
#         self.secure_adjacent = secure_adjacent
#         self.secure_nothing = secure_nothing
#         self.secure_other = secure_other
#         self.specify1 = specify1
#         self.modify = modify
#         self.usedPassword = usedPassword
#         self.not_changed1 = not_changed1
#         self.changed_slightly1 = changed_slightly1
#         self.changed_completly1 = changed_completly1
#         self.capatalized1 = capatalized1
#         self.addedwords = addedwords
#         self.deletedwords = deletedwords
#         self.number_N = number_N
#         self.number_changed_slightly = number_changed_slightly
#         self.number_changed_completly = number_changed_completly
#         self.number_added_digits = number_added_digits
#         self.number_deleted_digits = number_deleted_digits
#         self.number_substituted_digits = number_substituted_digits
#         self.number_O = number_O
#         self.char_N = char_N
#         self.char_changed_slightly = char_changed_slightly
#         self.char_changed_completly = char_changed_completly
#         self.char_added_symbols = char_added_symbols
#         self.char_deleted_symbols = char_deleted_symbols
#         self.char_substituted_symbols = char_substituted_symbols
#         self.char_O = char_O
#         self.userid = userid
#
#     def get_id(self):
#         return unicode(self.id)
#
#
# class Survey4(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     computerTime = db.Column(db.String(255))
#     pass_random = db.Column(db.Boolean)
#     pass_reuse = db.Column(db.Boolean)
#     pass_modify = db.Column(db.Boolean)
#     pass_new = db.Column(db.Boolean)
#     pass_substitute = db.Column(db.Boolean)
#     pass_multiword = db.Column(db.Boolean)
#     pass_phrase = db.Column(db.Boolean)
#     pass_O = db.Column(db.String(255))
#     how_regular_file = db.Column(db.Boolean)
#     how_encrypted = db.Column(db.Boolean)
#     how_software = db.Column(db.Boolean)
#     how_cellphone = db.Column(db.Boolean)
#     how_browser = db.Column(db.Boolean)
#     how_write_down = db.Column(db.Boolean)
#     how_no = db.Column(db.Boolean)
#     comments = db.Column(db.String(255))
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
#     user = db.relationship('User', uselist=False, backref='survey4')
#
#     def __init__(
#             self,
#             computerTime=None,
#             pass_random=None,
#             pass_reuse=None,
#             pass_modify=None,
#             pass_new=None,
#             pass_substitute=None,
#             pass_multiword=None,
#             pass_phrase=None,
#             pass_O=None,
#             how_regular_file=None,
#             how_encrypted=None,
#             how_software=None,
#             how_cellphone=None,
#             how_browser=None,
#             how_write_down=None,
#             how_no=None,
#             comments=None,
#             userid=None):
#
#         self.computerTime = computerTime
#         self.pass_random = pass_random
#         self.pass_reuse = pass_reuse
#         self.pass_modify = pass_modify
#         self.pass_new = pass_new
#         self.pass_substitute = pass_substitute
#         self.pass_multiword = pass_multiword
#         self.pass_phrase = pass_phrase
#         self.pass_O = pass_O
#         self.how_regular_file = how_regular_file
#         self.how_encrypted = how_encrypted
#         self.how_software = how_software
#         self.how_cellphone = how_cellphone
#         self.how_browser = how_browser
#         self.how_write_down = how_write_down
#         self.how_no = how_no
#         self.comments = comments
#         self.userid = userid
#
#     def get_id(self):
#         return unicode(self.id)
