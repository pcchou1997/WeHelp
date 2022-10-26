# -*- coding:utf-8 -*-

from flask import Flask
from flask import request
from flask import redirect
from flask import render_template
from flask import session
import mysql.connector

app = Flask(__name__)
app.secret_key = "any string but secret"

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    db='memberDB',
    charset='utf8mb4'
)
cursor = conn.cursor()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/signup", methods=["POST"])
def signup():
    # 得到user註冊資料
    name = request.values["register_name"]
    username = request.values["register_username"]
    password = request.values["register_password"]

    cursor.execute("SELECT *FROM member WHERE username=%s;", [username])
    datas = cursor.fetchall()
    if datas == []:
        if password == "" or name == "":
            return redirect("/error?message=註冊任一欄位不可留白")
        else:
            cursor.execute("INSERT INTO member(name,username,password)values(%s,%s,%s);", [
                name, username, password])
            conn.commit()  # 如果是insert、update、delete語句，需要加上這句
            cursor.execute("select *from member;")
            memberList = cursor.fetchall()
            return redirect("/")
    else:
        return redirect("/error?message=帳號已經被註冊")


@app.route("/signin", methods=["POST"])
def signin():
    # 取得表單輸入帳密
    account = request.form["acc"]
    password = request.form["pw"]
    # 篩選資料庫中有無輸入帳密這筆資料
    cursor.execute("SELECT id,name,username,password FROM member WHERE username=%s and password=%s;", [
                   account, password])
    signin_cmp = cursor.fetchall()  # 得到所有返回資料，fetchall或fetchone
    print(signin_cmp)
    # 若資料庫有此帳密，導至會員頁面
    if signin_cmp == []:
        return redirect("/error?message=帳號或密碼輸入錯誤")
    # 若資料庫無此帳密，導致失敗頁面
    else:
        name = signin_cmp[0][1]
        session["loginState"] = name
        session["name"] = name
        return redirect("/member")


@app.route("/member")
def member():
    name = session["name"]
    try:
        comment = session["message"]
        if session["loginState"] == name:
            return render_template("member.html", member_name=name, member_message=comment)
        else:
            return redirect("/")
    except KeyError:
        if session["loginState"] == name:
            return render_template("member.html", member_name=name, member_message="")
        else:
            return redirect("/")


@app.route("/error")
def error():
    msg = request.args.get("message", None)
    return render_template("error.html", message=msg)


@app.route("/signout", methods=["GET"])
def signout():
    session["loginState"] = ""
    return redirect("/")


@app.route("/message", methods=["POST"])
def message():
    name = session['loginState']
    content = request.form["content"]
    cursor.execute(
        "INSERT INTO message(message_name,message)values(%s,%s);", [name, content])
    conn.commit()
    cursor.execute("SELECT message_name,message FROM message")
    datas = cursor.fetchall()
    datas.reverse()
    session['message'] = datas
    return redirect("/member")


app.run(port=3000)
