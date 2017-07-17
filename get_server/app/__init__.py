from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route('/')
def send_file():
	return send_from_directory(directory='uploads', filename='NEW_APTnotes.csv', as_attachment=True)
