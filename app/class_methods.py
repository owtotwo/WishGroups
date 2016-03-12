from models import *
from app import db

# ========================= Member ===============================

def find_member_by_id(member_id):
	pass


# ========================== User ================================

def find_user_by_id(user_id):
	return User.query.get(user_id)

def find_user_by_name(user_name):
	return User.query.filter(User.username == user_name).first()

def add_user(username, password):
	db.session.add(User(username, password))
	db.session.commit()

def check_user(username, password):
	result = find_user_by_name(username)
	return result and result.password == password



# ========================== Wish ================================

	def find_wish_by_id(wish_id):
		return Wish.query.get(wish_id)

	def add_wish(body, wisher_id):
		pass


# ======================== Wishgroup =============================

def find_wishgroup_by_id(wishgroup_id):
	pass

def find_wishgroup_by_name(wishgroup_name):
	pass
