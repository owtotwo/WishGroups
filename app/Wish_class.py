from app import db

class Wish(db.Model):
	__tablename__ = 'wish'
	id = db.Column(db.Integer, primary_key = True)
	body = db.Column(db.String(140))

	group_id = db.Column(db.Integer, db.ForeignKey('wishgroup.id'))
	wisher_id = db.Column(db.Integer, db.ForeignKey('member.id'))
	implementer_id = db.Column(db.Integer, db.ForeignKey('member.id'))

# ------------------------------------------------------------------------------

	def __init__(self, body, wisher_id, implementer_id):
		self.body = body
		self.wisher_id = wisher_id
		self.implementer_id = implementer_id

	def __repr__(self):
		return '<Wish %r>' % (self.body)

# ------------------------------------------------------------------------------
'''
	def find_wish(wish_id):
		return Wish.query.get(wish_id)

	def add_wish(body, wisher_id, implementer_id = ADMIN.id):
		pass
'''