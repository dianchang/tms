# coding: utf-8
from datetime import datetime
from ._base import db


class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    avatar = db.Column(db.String(200))
    qrcode = db.Column(db.String(200))
    name = db.Column(db.String(50), unique=True)
    created_at = db.Column(db.DateTime, default=datetime.now)

    def __repr__(self):
        return '<Team %s>' % self.name


class UserTeam(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.now)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref=db.backref('teams',
                                                      lazy='dynamic',
                                                      order_by='desc(UserTeam.created_at)'))

    team_id = db.Column(db.Integer, db.ForeignKey('team.id'))
    team = db.relationship('Team', backref=db.backref('users',
                                                      lazy='dynamic',
                                                      order_by='desc(UserTeam.created_at)'))
