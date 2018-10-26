from flask import Flask,render_template,request,redirect,url_for
import sqlite3 as sql
app=Flask(__name__)

@app.route('/')
def home():
    return render_template('slide1.jinja2')
   

@app.route('/rooms/')
def rooms():
    return render_template('profess.jinja2')

@app.route('/rooms/addrooms/' , methods=['GET','POST'])
def addrooms():
    if request.method == 'POST':
        emp_id = request.form['empid']
        emp_name = request.form['empname']
        emp_age =   request.form['empage']
        emp_des = request.form['empdes']
        emp_phone = request.form['empphone']
        emp_address = request.form['empaddress']
        if emp_id.strip() is "" and emp_name.strip() is "" and emp_phone.strip() is "":
            return render_template('addprofess.jinja2', error="Enter all fields properly")
        else:
            try:
                with sql.connect("sqldb.db") as con:
                    cur = con.cursor()
                    cur.execute("create table if not exists profess (college_id INT primary key, name TEXT , age INT , branch TEXT , email TEXT ,contact TEXT)")
                    cur.execute("INSERT INTO profess (college_id,name,age,branch,email,contact) VALUES (?,?,?,?,?,?)", (emp_id,emp_name, emp_age, emp_des, emp_phone,emp_address))
                    con.commit()
                    msg = "Record saved successfully"
            except:
                con.rollback()
                msg = "Error in inserting record"
            finally:
                con.close()
                return render_template("addprofess.jinja2", msg=msg)
    return render_template('addprofess.jinja2')

@app.route('/rooms/lstroom/')
def lstrooms():
    with sql.connect("sqldb.db") as con:
        cur = con.cursor()
        cur.execute("select * from profess")
        roomlist = cur.fetchall()
    return render_template('listprofess.jinja2',roomlist=roomlist)

@app.route('/rooms/deleterooms/' , methods=['GET','POST'])
def deleterooms():
    if request.method == 'POST':
        empid=request.form['delbutton']
        print("this is the empid",int(empid))
        try:
            with sql.connect("sqldb.db") as con:
                cur = con.cursor()
                print("connection established\n\n\n\n")
                cur.execute("delete from profess where college_id=%d"%int(empid))
                print("sql function worked\n\n\n\n")
                con.commit()
                print("IT IS  commiting\n\n\n")
                con.close()
                print("successfully closed \n\n\n")
                return render_template("deleteprofess.jinja2")
        except:
            return render_template("deleteprofess.jinja2")
    else :
        return render_template("deleteprofess.jinja2")



app.run(debug=True)
