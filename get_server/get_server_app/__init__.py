from flask import Flask, send_from_directory

get_server = Flask(__name__)

@get_server.route('/')
def send_file():
	return send_from_directory(directory='uploads', filename='NEW_APTnotes.csv', as_attachment=True)
