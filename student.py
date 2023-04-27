from flask import Flask, render_template, request
from pymysql import connections
import os
import boto3
from config import *

app = Flask(__name__)

region = customregion

db_conn = connections.Connection(
    host=customhost,
    port=3306,
    user=customuser,
    password=custompass,
    db=customdb

)
output = {}
table = 'student'


@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template('AddEmp.html', title="University of South Florida")


@app.route("/about", methods=['POST'])
def about():
    return render_template('www.intellipaat.com')


@app.route("/addemp", methods=['POST'])
def AddEmp():
    uid = request.form['uid']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']

    insert_sql = "INSERT INTO employee VALUES (%s, %s, %s, %s, %s)"
    cursor = db_conn.cursor()

    try:
        cursor.execute(insert_sql, (uid, first_name, last_name, email, "University of South Florida"))
        db_conn.commit()
        student_name = "" + first_name + " " + last_name
    finally:
        cursor.close()

    print("all modification done...")
    return render_template('AddEmpOutput.html', name=student_name, uid=uid, email=email)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
