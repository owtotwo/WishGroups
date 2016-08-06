#!flask/bin/python
from app import app
from app.distribution import distribution_thread


# shuffle the wishes everyday
# distribution_thread.start()

app.run(host="192.168.1.105", port=8080, debug=True)
