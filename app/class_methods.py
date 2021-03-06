from app.models import *
from app import db

ADMIN_INNER_ID = 0

# ========================== Wish ================================

def find_wish_by_id(wish_id):
	return Wish.query.get(wish_id)

def add_wish(body, wisher_id):
	w = Wish(body, wisher_id)
	mem = Member.query.get(wisher_id)
	w.wishgroup_id = mem.wishgroup_id
	w.implementer_id = get_admin_by_id(mem.wishgroup_id).id # set to admin
	db.session.add(w)
	db.session.commit()


# ========================= Member ===============================

def find_member_by_id(member_id):
	return Member.query.get(member_id)

def add_member(user_id, wishgroup_id):
	wg = Wishgroup.query.get(wishgroup_id)
	next_inner_id = wg.members.order_by(Member.inner_id).all()[-1].inner_id + 1
	mem = Member(user_id, wishgroup_id, next_inner_id)
	db.session.add(mem)
	db.session.commit()

def get_admin_by_id(wishgroup_id):
	return Wishgroup.query.get(wishgroup_id)\
		.members.filter(Member.inner_id == ADMIN_INNER_ID).first()

def user_is_in_wishgroup(user_id, wishgroup_id):
	u = User.query.get(user_id)
	return wishgroup_id in [i.wishgroup_id for i in u.members]

def get_member_by_user_and_wishgroup(user_id, wishgroup_id):
	return Member.query.filter(Member.user_id == user_id,\
		Member.wishgroup_id == wishgroup_id).first()

def has_made_wish(member_id):
	mem = find_member_by_id(member_id)
	return len(mem.wishes.all()) > 0

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


# ======================== Wishgroup =============================

def all_wishgroups():
	return Wishgroup.query.order_by(Wishgroup.id).all()

def find_wishgroup_by_id(wishgroup_id):
	return Wishgroup.query.get(wishgroup_id)

def find_wishgroup_by_name(wishgroup_name):
	return Wishgroup.query.filter(Wishgroup.name == wishgroup_name).first()

def add_wishgroup(user_id, wishgroup_name):
	# create a admin with inner id of zero when add a new wishgroup
	wg = Wishgroup(wishgroup_name)
	db.session.add(wg)
	wishgroup_id = find_wishgroup_by_name(wishgroup_name).id
	inner_id = ADMIN_INNER_ID
	admin = Member(user_id, wishgroup_id, inner_id)
	db.session.add(admin)
	db.session.commit()

def get_members_from_wishgroup_by_id(wishgroup_id):
	result = Member.query.filter(Member.wishgroup_id == wishgroup_id).all()
	return sorted(result, key = (lambda x: x.inner_id))


# ======================== Unknown =============================
from random import shuffle

def distribute_wish(wishgroup_id):
	# for each member as well as wisher in wishgroup, shuffle their id 
	# and map them to others.
	wg = find_wishgroup_by_id(wishgroup_id)
	wishes_id = [x.id for x in wg.wishes]
	if len(wishes_id) < 2:
		return 0
	shuffle(wishes_id)
	for i in range(len(wishes_id) - 1):
		find_wish_by_id(wishes_id[i]).implementer_id = find_wish_by_id(wishes_id[i + 1]).wisher_id
	find_wish_by_id(wishes_id[-1]).implementer_id = find_wish_by_id(wishes_id[0]).wisher_id
	db.session.commit()
	return len(wishes_id)


def distribute_all_wish():
	for i in all_wishgroups():
		print("Distributing WishGroup " + str(i.id) + "...", end="")
		print(str(distribute_wish(i.id)) + " Wishes...", end="")
		print("Done!")
