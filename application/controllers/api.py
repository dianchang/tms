# coding: utf-8
from flask import Blueprint, render_template
from ..models import User
from ..utils.decorators import jsonify

bp = Blueprint('api', __name__)


@bp.route('/api/user/<int:uid>/feeds')
@jsonify
def user_feeds(uid):
    user = User.query.get_or_404(uid)
    return [{'id': feed.id,
             'kind': feed.kind,
             'text': feed.text,
             'punch': feed.punch,
             'image': feed.image} for feed in user.feeds]


@bp.route('/api/signin', methods=['POST'])
def signin():
    pass
