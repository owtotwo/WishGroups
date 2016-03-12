from flask import render_template, request, redirect, url_for, flash
from flask.ext import login
from app import app, login_manager
from class_methods import *
from .forms import RegistrationForm, LoginForm

@login_manager.user_loader
def load_user(user_id):
	return find_user_by_id(user_id)

@app.errorhandler(404)
def not_found(error):
	print "Error %s: Can\'t not found this page." % (error)
	return render_template('404.html')

# ----------------------------------------------------------



@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html', current_user = login.current_user)


@app.route('/login', methods = ['GET', 'POST'])
def log_in():
	form = LoginForm(request.form)
	if request.method == 'POST' and form.validate():
		if check_user(form.username.data, form.password.data):
			login.login_user(find_user_by_name(form.username.data))
			flash('Success to Login.')
			print 'Success to Login.'
			print 'current username is ' + login.current_user.username
			return redirect(url_for('index'))

		else:
			flash('Fail to Login.')

	return render_template('login.html', \
		form = form, current_user = login.current_user)



@app.route('/logout')
@login.login_required
def log_out():
	login.logout_user()
	return redirect(url_for('index'))



@app.route('/register', methods = ['GET', 'POST'])
def register():
	form = RegistrationForm(request.form)

	if request.method == 'POST' and form.validate():

		if not find_user_by_name(form.username.data):
			add_user(form.username.data, form.password.data)
			flash('Thanks for registering')
			return redirect(url_for('log_in'))
		else:
			flash('This username has already been used.')

	return render_template('register.html', \
		form = form, current_user = login.current_user)



@app.route('/info')
@login.login_required
def user_info():
	return render_template('user_info.html', \
		current_user = login.current_user)


@app.route('/join_group')
@login.login_required
def join_group():
	pass

@app.route('/group_list')
@login.login_required
def group_list():
	return render_template('group_list.html',\
		current_user = login.current_user,\
		all_wishgroups = all_wishgroups,\
		user_wishgroups = [i.wishgroup for i in login.current_user.members])
