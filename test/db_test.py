#!../flask/bin/python
import sys
sys.path.append('../')

from app import db, models
from sqlalchemy import text

def add_user(uname, pwd):
	u = models.User(username = uname, password = pwd)
	
	if u.username in [i.username for i in models.User.query.all()]:
		print 'User %s is already Signed up.' % (u.username)
	else:
		db.session.add(u)
		db.session.commit()
		print 'Success to add User %s.' % (u.username)

def main():
	print models.User.query.as_scalar()
	print models.User.query.count()
	print models.User.query.from_statement(text('select * from user where username = \"Tom\"')).all()
	print models.User.query.cte()
	#add_user('Tom', '123')
	#add_user('Jack', '456')

if __name__ == '__main__':
	main()
