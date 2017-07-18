#!flask/bin/python
from get_server_app import get_server

context = ('fullchain.pem', 'privkey.pem')

get_server.run(debug=None, host='0.0.0.0', port='443', ssl_context=context)
