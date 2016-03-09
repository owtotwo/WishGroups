from app import db
import models
from sqlalchemy import text

def find_user(uname):
	lis = models.User.query.from_statement(
		text('select * from user where username = \"%s\"' % (uname))).all()
	if lis:
		return lis[0]
	else:
		return None

def add_user(uname, pwd):
	u = models.User(username = uname, password = pwd)
	
	if find_user(u.username):
		print 'User %s is already Signed up.' % (u.username)
		return False
	else:
		db.session.add(u)
		db.session.commit()
		print 'Success to add User %s.' % (u.username)
		return True


def remove_user(uname):	
	u = find_user(uname)
	if u:
		db.session.delete(u)
		db.session.commit()
		return True
	else:
		print 'No this User'
		return False