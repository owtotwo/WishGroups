from app import db
from datetime import datetime

class Wish(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	body = db.Column(db.String(140))
	state = db.Column(db.String(20))
	timestamp = db.Column(db.DateTime)
	group_id = db.Column(db.Integer, db.ForeignKey('Group.id'))
	wisher_id = db.Column(db.Integer, db.ForeignKey('Member.id'))
	implementer_id = db.Column(db.Integer, db.ForeignKey('Member.id'))

# ------------------------------------------------------------------------------

	def __init__(self, body, wisher_id):
		self.body = body
		self.state = WISH_STATE_WAITING_FOR_IMPLEMENTER
		self.timestamp = int(datetime.now().timestamp())
		self.wisher_id = wisher_id
		self.implementer_id = implementer_id

	def __repr__(self):
		return '<Wish %r>' % (self.body)

# ------------------------------------------------------------------------------

	def find_wish(wish_id):
		return Wish.query.get(wish_id)

	def add_wish(body, wisher_id, implementer_id = ADMIN.id):
