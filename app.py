from flask import Flask, render_template,request
import sqlite3
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('checkin.html', room="location")

@app.route('/TLC109')
def tlc109():
    return render_template('checkin.html', room="TLC109")

@app.route('/TLC110')
def tlc110():
    return render_template('checkin.html', room="TLC110")

@app.route('/TLC111')
def tlc111():
    return render_template('checkin.html', room="TLC111")

@app.route('/checkedin',methods=['GET', 'POST'])
def checkedin():

    con = sqlite3.connect("DIGSOLN11.db", check_same_thread=False)
    cur = con.cursor()

    if request.method == 'POST':
        room = request.form["room"]
        print(room)
        student_email = request.form["eq_email"]
        date = datetime.now().strftime("%d/%m/%Y")
        time =  datetime.now().strftime("%H:%M:%S")
        student_id = student_email.split('@')[0]
        query = f"SELECT Firstname,Lastname FROM Year11Students WHERE studentId = '{student_id}'"
        cur.execute(query)
        result = cur.fetchone()

        ## If there's a student match
        if result != None:
            student = result[1] + ' ' + result[0]
            query = f"INSERT INTO SignedIn VALUES('{student_id}', '{date}', '{time}', '{room}')"
            print(student_id, date, time, room)
            cur.execute(query)
            con.commit()
    else:
        student = "Jack, Jackson"

    return render_template('complete.html', student=student)
    con.close()


