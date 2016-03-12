from models import *
from app import db

# ========================= Member ===============================

def find_member_by_id(member_id):
	return Member.query.get(member_id)

def add_member():
	pass

def get_admin_by_id(wishgroup_id):
	return Wishgroup.query.get(wishgroup_id)\
		.members.filter(Member.inner_id == 0).first()

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

def all_wishgroups():
	return Wishgroup.query.all()

def find_wishgroup_by_id(wishgroup_id):
	return Wishgroup.query.get(wishgroup_id)

def find_wishgroup_by_name(wishgroup_name):
	return Wishgroup.query.filter(Wishgroup.name == wishgroup_name).first()

def add_wishgroup():
	pass
