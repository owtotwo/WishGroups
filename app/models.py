from app import db

class User(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	username = db.Column(db.String(64), index = True, unique = True)
	password = db.Column(db.String(20), index = True, unique = True)
	wishes = db.relationship('Wish', backref = 'author', lazy = 'dynamic')

	def get_id(self):
		return unicode(self.id)

	def __repr__(self):
		return '<User %r>' % (self.username)


class Wish(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	body = db.Column(db.String(140))
	timestamp = db.Column(db.DateTime)
	user_id = db.Column(db.Integer, db.ForeignKey('User.id')) # or user.id?

	def __repr__(self):
		return '<Wish %r>' % (self.body)
