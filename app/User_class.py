from app import db
import flask_login as login
from app.Member_class import Member

class User(db.Model, login.UserMixin):
	__tablename__ = 'user'
	id = db.Column(db.Integer, primary_key = True)
	username = db.Column(db.String(128), index = True, unique = True)
	password = db.Column(db.String(20))
	members = db.relationship('Member', backref = 'user', lazy = 'dynamic')

# ------------------------------------------------------------------------------
	def __init__(self, username, password):
		self.username = username
		self.password = password

	def __repr__(self):
		return '<User %r>' % (self.username)

