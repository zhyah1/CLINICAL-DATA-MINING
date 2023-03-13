from flask import*

from src.dbconnection import *

app=Flask(__name__)
app.secret_key="qwe"


@app.route('/')
def main():
    # return render_template('adminindex.html')
    return render_template('login.html')
@app.route('/edit_doc')
def edit_doc():
    id=request.args.get('id')
    session['eid']=id
    qry="SELECT * FROM `doctor` WHERE d_id=%s"
    val=(str(id))
    res=selectone(qry,val)
    return render_template('HOSPITAL/editdoc.html',val=res)

@app.route('/delete_doc')
def delete_doc():
    id=request.args.get('id')
    q="DELETE FROM `login` WHERE id=%s"
    v=(str(id))
    iud(q,v)
    qry="DELETE FROM `doctor` WHERE `l_id`=%s"
    val=(str(id))
    iud(qry,val)
    return '''<script>alert("Data deleted successfully");window.location = "/manage_doctor" </script>'''



@app.route('/update_doc',methods=['post'])
def update_doc():
    dept = request.form['select']
    fname = request.form['textfield']
    lname = request.form['textfield2']
    gender = request.form['radiobutton']
    quali = request.form.getlist('checkbox')
    qua = ",".join(quali)

    dob = request.form['textfield3']
    exp = request.form['textfield4']
    place = request.form['textfield42']
    post = request.form['textfield43']
    pin = request.form['textfield44']
    mail = request.form['textfield45']
    cntct = request.form['textfield46']
    id=session['eid']
    qry1 = "UPDATE `doctor` SET `first_name`=%s,`last_nmae`=%s,`dept_name`=%s,`gender` =%s,`qualification` =%s,`dob` =%s,`experiance` =%s,`place` =%s,`post` =%s,`pin` =%s,`email` =%s,`contact` =%s WHERE `d_id`=%s"
    val1 = (fname, lname, dept, gender, qua, dob, exp, place, post, pin, mail, cntct,id)
    iud(qry1, val1)
    return '''<script>alert("Data updated successfully");window.location = "/manage_doctor" </script>'''


@app.route('/login',methods=['post'])
def login():
    uname=request.form['uname']
    password=request.form['psw']
    qry="SELECT * FROM `login` WHERE(`user_name` = %s AND `password` = %s)"
    val=(uname,password)
    res=selectone(qry,val)
    if res is None:
        return'''<script>alert("invalid");window.location = "/" </script>'''
    elif res[3]=='admin':
        session['lid']=res[0]
        return'''<script>alert("welcome");window.location = "/hospital_home" </script>'''
    elif res[3]=='doctor':
        session['lid'] = res[0]
        return '''<script>alert("welcome");window.location = "/doctor_home" </script>'''


    else:
        return'''<script>alert("invalid");window.location = "/" </script>'''

@app.route('/doc_reg',methods=['post'])
def doc_reg():
    hid=session['lid']
    dept=request.form['select']
    fname=request.form['textfield']
    lname=request.form['textfield2']
    gender=request.form['radiobutton']
    quali=request.form.getlist('checkbox')
    qua=",".join(quali)

    dob=request.form['textfield3']
    exp=request.form['textfield4']
    place=request.form['textfield42']
    post=request.form['textfield43']
    pin=request.form['textfield44']
    mail=request.form['textfield45']
    cntct=request.form['textfield46']
    uname=request.form['textfield5']
    password=request.form['textfield6']
    qry="INSERT INTO `login` VALUES(NULL,%s,%s,'doctor')"
    val=(uname,password)
    lid=iud(qry,val)
    qry1="INSERT INTO `doctor` VALUES(NULL,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    val1=(str(lid),str(hid),fname,lname,dept,gender,qua,dob,exp,place,post,pin,mail,cntct)
    iud(qry1,val1)
    return '''<script>alert("Data added successfully");window.location = "/hospital_home" </script>'''


@app.route('/add_drug_info',methods=['post'])
def add_drug_info ():
    return render_template('DOCTOR/add drug info.html')


@app.route('/add_drug',methods=['post'])
def add_drug():
    did=session['lid']
    drgname = request.form['textfield3']
    expdate=request.form['textfield']
    manudate=request.form['textfield2']
    desc=request.form['textfield4']
    qry="INSERT INTO `medicine` VALUES(NULL,%s,%s,%s,%s,%s)"
    val=(str(did),expdate,manudate,drgname,desc)
    iud(qry,val)
    return '''<script>alert("Drug added successfully");window.location = "/manage_drug_info" </script>'''

@app.route('/drug_edit')
def drug_edit():
    id=request.args.get('id')
    session['id']=id
    qry="SELECT * FROM `medicine` WHERE `medicine_id`=%s"
    val=(str(id))
    res=selectone(qry,val)
    return render_template('DOCTOR/edit drug info.html',val=res)


@app.route('/drug_delete')
def drug_delete():
    id=request.args.get('id')
    qry="DELETE FROM `medicine`WHERE `medicine_id`=%s"
    val=(str(id))
    iud(qry,val)
    return'''<script>alert("Drug added successfully");window.location = "/manage_drug_info" </script>'''



@app.route('/edit_drug',methods=['post'])
def edit_drug():
    drgname = request.form['textfield']
    expdate = request.form['textfield2']
    manudate = request.form['textfield3']
    desc = request.form['textfield4']
    qry="UPDATE `medicine` SET `drug_name`=%s,`exp_date`=%s,`manfac_date`=%s,`description`=%s WHERE `medicine_id`=%s"
    val=(drgname,expdate,manudate,desc,session['id'])
    iud(qry,val)
    return '''<script>alert("Drug Edited successfully");window.location = "/manage_drug_info" </script>'''

@app.route('/chat_with_user')
def chat_with_user ():
    qry="SELECT `user`.`first_name`,`user`.`last_name` FROM `user`"
    res=selectall(qry)
    return render_template('DOCTOR/chat with user.html',val=res)

@app.route('/doctor_home')
def doctor_home ():
    return render_template('DOCTOR/doctor home.html')

@app.route('/manage_drug_info')
def manage_drug_info ():
    qry = "SELECT * FROM `medicine`"
    val = selectall(qry)
    return render_template('DOCTOR/manage drug info.html',res=val)

@app.route('/view_booking')
def view_booking ():
    qry="SELECT `user`.`first_name`,`user`.`last_name`,`booking`.`date`, `user`.`l_id` FROM `user` JOIN `booking`ON `user`.`l_id`=`booking`.`user_id`"
    res=selectall(qry)
    return render_template('DOCTOR/view booking.html',val=res)

@app.route('/view_schedule')
def view_schedule ():
    qry="SELECT * FROM`schedule`"
    res = selectall(qry)
    return render_template('DOCTOR/view schedule.html',val=res)

@app.route('/add_doctor')
def add_doctor ():
    return render_template('HOSPITAL/Add doctor.html')

@app.route('/manage_booking')
def manage_booking():
    qry="SELECT `booking`.*,`user`.`first_name`,`user`.`last_name`,`doctor`.`first_name`,`doctor`.`last_nmae`,`schedule`.`date`,`from_time`,`to_time` FROM `booking` JOIN `schedule` ON `booking`.`schedule`=`schedule`.`s_id` JOIN `doctor` ON `doctor`.`l_id`=`schedule`.`doctor_id` JOIN `user` ON `user`.`l_id`=`booking`.`user_id` WHERE `booking`.status='pending'"
    res=selectall(qry)
    return render_template('HOSPITAL/manage booking.html',val=res)



@app.route('/accept_booking')
def accept_booking():
    bid=request.args.get('id')
    qry="UPDATE `booking` SET `status`='booked' WHERE `book_id`=%s"
    val=(bid)
    iud(qry,val)
    return redirect('/manage_booking')

@app.route('/reject_booking')
def reject_booking():
    bid=request.args.get('id')
    qry="UPDATE `booking` SET `status`='rejected' WHERE `book_id`=%s"
    val=(bid)
    iud(qry,val)
    return redirect('/manage_booking')


@app.route('/manage_doctor')
def manage_doctor():
    qry="SELECT * FROM `doctor`"
    res=selectall(qry)

    return render_template('HOSPITAL/managedoctor.html',val=res)

@app.route('/schedule_doctor')
def schedule_doctor():
    qry="SELECT * FROM `doctor`"
    res=selectall(qry)
    return render_template('HOSPITAL/Schedule doctor.html',val=res)

@app.route('/doc_schedule',methods=['post'])
def doc_schedule():
    doc= request.form['select']
    date= request.form['textfield462']
    frmtime= request.form['textfield46']
    totime= request.form['textfield463']
    qry="INSERT INTO `schedule` VALUES (NULL,%s,%s,%s,%s)"
    val=(doc,date,frmtime,totime)
    iud(qry,val)
    return '''<script>alert("Scheduled successfully");window.location = "/schedule_doctor" </script>'''




@app.route('/view_users')
def view_users():
    qry="SELECT *FROM `user`"
    res=selectall(qry)
    return render_template('HOSPITAL/view users.html',val=res)
@app.route('/hospital_home')
def hospital_home():
    return render_template('HOSPITAL/hospital home.html')
@app.route('/report')
def report():

    id = request.args.get('id')
    session['id']=id
    qry ="SELECT `doctor`.`first_name`,`doctor`.`last_nmae`,`report`.`date`,`report`.`report` FROM `doctor` JOIN `report` ON `doctor`.`l_id`=`report`.`doctor_id` WHERE `report`.`user_id`=%s"
    val =(id)
    res = selectall2(qry, val)
    return render_template('DOCTOR/report.html',val=res)
@app.route('/upload',methods=['post'])
def upload():
    return render_template('DOCTOR/upload.html')
@app.route('/uploadreport',methods=['post'])
def uploadreport():
    file=request.files['file']
    fn=file.filename
    file.save("static/report/"+fn)
    qry="INSERT INTO `report` VALUES(NULL,%s,%s,CURDATE(),%s)"
    val=(session['id'],session['lid'],fn)
    iud(qry,val)
    return render_template('DOCTOR/upload.html')














app.run(debug=True)
