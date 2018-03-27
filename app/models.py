# -*- coding: utf-8 -*-

from mixins import CRUDMixin
from flask.ext.login import UserMixin

from app import db

import datetime


ROLE_USER = 0
ROLE_ADMIN = 1


class User(UserMixin, CRUDMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    userid = db.Column(db.String(255), unique=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(20))
    oldPassword = db.Column(db.String(20))
    changedPass = db.Column(db.Boolean)
    role = db.Column(db.SmallInteger, default=ROLE_USER)
    s1 = db.Column(db.Boolean)
    s2 = db.Column(db.Boolean)
    s3 = db.Column(db.Boolean)
    s4 = db.Column(db.Boolean)
    lastSeen = db.Column(db.String(255))

    def __init__(
            self,
            email=None,
            userid=None,
            password=None,
            oldPassword=None,
            changedPass=False,
            s1=False,
            s2=False,
            s3=False,
            s4=False,
            role=None):
        self.email = email
        self.userid = userid
        self.password = password
        self.oldPassword = oldPassword
        self.changedPass = changedPass
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
        self.s4 = s4
        self.role = role

    def is_admin(self):
        if self.role == 1:
            return True
        else:
            return False

    def is_active(self):
        return True

    def get_id(self):
        return unicode(self.id)

    def __repr__(self):
        return '<User %r>' % (self.email)


class PersonalSurvey(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(8), nullable=False)
    date = db.Column(db.Date)
    year = db.Column(db.Integer,nullable=False,default=2018)

    def __init__(
            self,
            username,
            year=datetime.datetime.utcnow().year):
        self.date = datetime.datetime.utcnow()
        self.year = year
        self.username=username



    def get_id(self):
        return unicode(self.id)

    @staticmethod
    def has_been_done_by(username, year=None):

        q= PersonalSurvey.query.filter(PersonalSurvey.username==username)
        if year:
            q=q.filter(PersonalSurvey.year==year)

        if q.count()>0:
            return True,q.all()

        return False,[]


class SharedSurvey(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(8), nullable=False)
    date = db.Column(db.Date)
    year = db.Column(db.Integer,nullable=False,default=2018)

    def __init__(
            self,
            username,
            year=datetime.datetime.utcnow().year):
        self.date = datetime.datetime.utcnow()
        self.year = year
        self.username=username

    def get_id(self):
        return unicode(self.id)

    @staticmethod
    def has_been_done_by(username, year=None):

        q= PersonalSurvey.query.filter(PersonalSurvey.username==username)
        if year:
            q=q.filter(PersonalSurvey.year==year)

        if q.count>0:
            return True,q.all()

        return False,[]

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
