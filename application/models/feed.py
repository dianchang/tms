# coding: utf-8
from datetime import datetime
from ._base import db


class Feed(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    kind = db.Column(db.Enum('location', 'text', 'image', 'punch'), nullable=False)
    location = db.Column(db.String(200))
    text = db.Column(db.String(500))
    image = db.Column(db.String(200))
    punch = db.Column(db.String(50))
    created_at = db.Column(db.DateTime, default=datetime.now)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref=db.backref('feeds',
                                                      lazy='dynamic',
                                                      order_by='desc(UserTeam.created_at)'))

    team_id = db.Column(db.Integer, db.ForeignKey('team.id'))
    team = db.relationship('Team', backref=db.backref('feeds',
                                                      lazy='dynamic',
                                                      order_by='desc(UserTeam.created_at)'))

    def __repr__(self):
        return '<Feed %s>' % self.name
