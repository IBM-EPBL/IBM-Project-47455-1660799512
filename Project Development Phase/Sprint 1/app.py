from flask import Flask, render_template, request, url_for, redirect
from flask_mysqldb import MySQL

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
        return redirect(url_for("home"))
    return render_template("register.html")


if (__name__ == '__main__'):
    app.secret_key="012#!@(ApajdCMJNDc/"
    app.run(debug=True)

