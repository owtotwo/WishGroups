from threading import Thread, Timer
from time import sleep
from datetime import datetime, timedelta
from app.class_methods import distribute_all_wish
from config import DISTRIBUTE_HOUR, DISTRIBUTE_MIN, DISTRIBUTE_SEC

def distribute_on_time(hour, minute, second):
	while True:
		now = datetime.now()
		dist = datetime(now.year, now.month, now.day, hour, minute, second)
		if now > dist:
			dist += timedelta(days=1)
		tmp = int((dist - now).total_seconds())
		print("Sleep " + str(tmp) + "s...")
		sleep(tmp)
		distribute_all_wish()
		sleep(2)


distribution_thread = Thread(target=distribute_on_time, \
    args=(DISTRIBUTE_HOUR, DISTRIBUTE_MIN, DISTRIBUTE_SEC))
