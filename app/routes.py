from app.entities import ChatLine
from datetime import datetime
from flask import render_template, session, url_for, jsonify, request, make_response, redirect
from app import app

from os import path
BASE_DIR = path.dirname(path.realpath(__file__))

def areValidateInputs(userIn, msgIn):
    return userIn and msgIn and not '\n' in userIn and not '\n' in msgIn

@app.route('/')
@app.route('/<room>')
def index(room='general'):
    session.clear()
    return render_template('index.html')

@app.route('/api/chat/', methods=['GET', 'POST'])
@app.route('/api/chat/<room>', methods=['GET', 'POST'])
def api(room=''):
    if not room:
        return redirect(url_for('api', room='general'), code=307)
    filePath=BASE_DIR+"/rooms/"+room
    if session.get('errors'):
        roomData=session['errors']
    else:
        roomData=""
    if request.method == 'POST':
        usernameInput=request.form.get("username")
        messageInput=request.form.get("msg")
        if areValidateInputs(usernameInput, messageInput):
            openMode='a'
            if not path.exists(filePath):
                openMode='w'
            with open(filePath, openMode) as roomFile:
                chatLine=ChatLine(usernameInput, messageInput, datetime.now())
                roomFile.write(f'{chatLine}\n')
            session.clear()
        else:
            session['errors']="<username> and <message> inputs can't be empty and can't contain new line!\n"
    if path.exists(filePath):
        with open(filePath, 'r') as file:
            lines = file.readlines()
            for line in reversed(lines):
                roomData+=line
    else:
        roomData+="[No new posts]"
    response = make_response(roomData, 200)
    response.mimetype = "text/plain"
    return response

@app.route('/chat/', methods=['GET', 'POST'])
@app.route('/chat/<room>', methods=['GET', 'POST'])
def chat(room=''):
    session.clear()
    if not room:
        room="general"
    return redirect(url_for('api', room=room), code=307)