from flask import Flask, render_template, request, url_for, redirect
from flask_mysqldb import MySQL
import smtplib

app = Flask(__name__)
# mysql configuration
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "123456789"
app.config["MYSQL_DB"] = "crud"
app.config["MYSQL_CURSORCLASS"] = "DictCursor"
mysql = MySQL(app)
if (mysql):
    print("db connected")
else:
    print("not connected")


@app.route("/")
def home():
    return render_template("home.html")
@app.route("/login",methods=['GET','POST'])
def login():
    return render_template("login.html")
#new user

@app.route("/add",methods=['GET','POST'])
def add():
    if request.method=='POST':
        name= request.form['name']
        age = request.form['age']
        gender =request.form['gender']
        email= request.form['email']
        password = request.form['password']
        phone = request.form['phone']
        con=mysql.connection.cursor()
        sql="insert into new_table3(NAME,AGE,GENDER,EMAIL,PASSWORD,PHONE) value(%s ,%s ,%s, %s ,%s ,%s)"

        con.execute(sql,[name,age,gender,email,password,phone])
        mysql.connection.commit()
        con.close()
        message= "Thank you for register in heart disease prediction app"
        server=smtplib.SMTP("smtp.gmail.com",587)
        server.starttls()
        server.login("19cst002@acetcbe.edu.in","vijayaragavandev")
        server.sendmail("19cst002@acetcbe.edu.in",email,message)
        return redirect(url_for("home"))
    return render_template("register.html")

@app.route("/editUser/<string:id>",methods=['GET','POST'])
def editUser(id):
    return render_template("editUser.html")

@app.route("/admin")
def admin():
    con = mysql.connection.cursor()
    sql = "SELECT * FROM new_table3"
    con.execute(sql)
    res = con.fetchall()
    return render_template("admin.html",datas=res)

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")
if (__name__ == '__main__'):
    app.secret_key="012#!@(ApajdCMJNDc/"
    app.run(debug=True)