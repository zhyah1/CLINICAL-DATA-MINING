from flask import*

from src.dbconnection import *

app=Flask(__name__)
@app.route('/login')
def login():
    username = request.form['username']
    password=request,form['password']
    qry="SELECT * FROM `login`WHERE `user_name`=%s AND `password`=%s"
    val=(username,password)
    res=selectone(qry,val)
    if res is None:
        return jsonify{"task":""}
    elif res[3]=='user':
        return jsonify{"task":"success"}
