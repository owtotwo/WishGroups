#!flask/bin/python
from app import app
from app.distribution import distribution_thread

# shuffle the wishes everyday
distribution_thread.start()

# if use_reloader is True, it will restart the app and make some wrong
# in the threads, which will cause the distribution_thread runs twice.
app.run(host="192.168.1.105", port=8080, debug=True, use_reloader=False)
