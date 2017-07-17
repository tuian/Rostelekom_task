#!flask/bin/python
from app import app

context = ('/etc/letsencrypt/live/iocs.tk/fullchain.pem', '/etc/letsencrypt/live/iocs.tk/privkey.pem')


app.run(debug=None, host='0.0.0.0', port='443', ssl_context=context)
