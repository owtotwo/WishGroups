from app import db, models


def add_user(uname, pwd):
	u = models.User(username = uname, password = pwd)
	
	if u.username in [i.username for i in models.User.query.all()]:
		print 'User %s is already Signed up.' % (u.username)
		return False
	else:
		db.session.add(u)
		db.session.commit()
		print 'Success to add User %s.' % (u.username)
		return True