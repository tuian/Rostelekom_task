#!flask/bin/python
from get_server_app import get_server

# context = ('/etc/letsencrypt/live/iocs.tk/fullchain.pem', '/etc/letsencrypt/live/iocs.tk/privkey.pem')


# get_server.run(debug=None, host='0.0.0.0', port='443', ssl_context=context)
get_server.run(host='0.0.0.0', port='80')

