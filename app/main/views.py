from . import main
from flask_login import login_required
from flask import render_template, request,flash


@main.route('/')
@login_required
def index():
	return render_template('index.html')


@main.route('/admin')
@login_required
def for_admins_only():
	return "管理员"


@main.route('/moderator')
@login_required
def for_moderators_only():
	return "评论修改者"


@main.route('/user')
@login_required
def userinfo():
	return render_template('user.html')


