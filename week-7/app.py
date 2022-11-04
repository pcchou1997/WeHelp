# -*- coding:utf-8 -*-

from flask import Flask
from flask import request
from flask import redirect
from flask import render_template
from flask import session
import mysql.connector
from flask import jsonify
import json

app = Flask(__name__)
app.secret_key = "any string but secret"


conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Aaa-860221',
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
        if password == "" or name == "" or username == "":
            return redirect("/error?message=註冊任一欄位不可留白")
        else:
            cursor.execute("INSERT INTO member(name,username,password)values(%s,%s,%s);", [
                name, username, password])
            conn.commit()  # 如果是insert、update、delete語句，需要加上這句，執行到這句才是真正改變資料庫，之前只是暫存在內存
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
    # 若資料庫有此帳密，導至會員頁面
    if signin_cmp == []:
        return redirect("/error?message=帳號或密碼輸入錯誤")
    # 若資料庫無此帳密，導致失敗頁面
    else:
        name = signin_cmp[0][1]
        usrname = signin_cmp[0][2]
        session["loginState"] = name
        session["usrname"] = usrname
        return redirect("/member")


@app.route("/member")
def member():
    # 確認有登入資訊且為本人
    if session["loginState"] != "":
        return render_template("member.html", member_name=session["loginState"])
    else:
        return redirect("/")


@app.route("/error")
def error():
    msg = request.args.get("message", None)
    return render_template("error.html", message=msg)


@app.route("/signout", methods=["GET"])
def signout():
    session["loginState"] = ""
    session["usrname"] = ""
    return redirect("/")


@app.route("/message", methods=["POST"])
def message():
    name = session['loginState']
    content = request.form["content"]
    cursor.execute(
        "INSERT INTO message(message_name,message)values(%s,%s);", [name, content])
    conn.commit()
    return redirect("/member")


@app.route("/api/member", methods=["GET", "PATCH"])
def api_member():
    name = session["loginState"]
    usrname = session["usrname"]
    if request.method == "GET":
        outDict = {}
        searchName = request.args.get("searchUsername", None)
        cursor.execute(
            "SELECT id,name,username FROM member WHERE username=%s;", [searchName])
        searchNameList = cursor.fetchall()
        try:
            if session["loginState"] != "" and searchNameList != []:
                for each in searchNameList:
                    inDict = {}
                    inDict['id'] = each[0]
                    inDict['name'] = each[1]
                    inDict['username'] = each[2]
                    outDict['data'] = inDict
            else:
                outDict['data'] = None

        except:
            outDict['data'] = None
        finally:
            outDict = jsonify(outDict)
            return outDict
    if request.method == "PATCH":
        newname = request.get_json()
        cursor.execute(
            "SELECT id,name,username FROM member WHERE username=%s;", [usrname])
        nameList = cursor.fetchall()
        if session["loginState"] != "" and nameList != []:
            cursor.execute(
                "UPDATE member SET name=%s WHERE username=%s", [newname["name"], usrname])
            conn.commit()
            changeRes = {"ok": True}
            return jsonify(changeRes)
        else:
            changeRes = {"error": True}
            return jsonify(changeRes)


app.run(port=3000, debug=True)  # debug=True 代表存擋後自動重啟程式
