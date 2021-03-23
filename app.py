from flask import Flask, render_template,request
from flask_socketio import SocketIO, send

import os
port = int(os.environ.get('PORT', 5000))

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'
socketio = SocketIO(app, cors_allowed_origins='*')

## LOAD IN THE SWEAR LIST
swearList = []
with open ("swearlist.txt", 'r') as swearfile:
	for line in swearfile:
		swearList.append(line.strip())

@socketio.on('message')
def handleMessage(msg):
	print('Message: ' + msg)

	## If you say a word from the list, say "No Swearing"
	for word in msg.split(' '):
		## Swear Alert
		if word.lower() in swearList:
			msg = "NO SWEARING"
	send(msg, broadcast=True)

@app.route('/')
def sessions():
    return render_template('main.html')

if __name__ == '__main__':
	socketio.run(app, host="0.0.0.0",port=port)
