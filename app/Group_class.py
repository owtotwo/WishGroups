from app import db
from Member_class import Member
from Wish_class import Wish

class Wishgroup(db.Model):

	__tablename__ = 'wishgroup'

	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(120), index = True, unique = True)
	
	members = db.relationship('Member', lazy = 'dynamic', backref = 'wishgroup')
	wishes = db.relationship('Wish', lazy = 'dynamic', backref = 'wishgroup')

	def __init__(self, name):
		self.name = name

	def __repr__(self):
		return '<Group %r>' % (self.name)

