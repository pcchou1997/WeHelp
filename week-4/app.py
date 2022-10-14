from flask import Flask
from flask import request
from flask import redirect
from flask import render_template
from flask import session

app = Flask(__name__)
app.secret_key = "any string but secret"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/member")
def member():
    if session["loginState"] == True:
        return render_template("member.html")
    else:
        return redirect("/")


@app.route("/error")
def error():
    msg = request.args.get("message", None)
    return render_template("error.html", message=msg)


@app.route("/signin", methods=["POST"])
def signin():
    account = request.form["acc"]
    password = request.form["pw"]
    if account == "test" and password == "test":
        session["loginState"] = True
        return redirect("/member")
    elif account == "" or password == "":
        return redirect("/error?message=請輸入帳號、密碼")
    else:
        return redirect("/error?message=帳號、或密碼輸入錯誤")


@app.route("/signout", methods=["GET"])
def signout():
    session["loginState"] = False
    return redirect("/")


@app.route("/square")
def preSquare():
    num = request.args.get("num", None)
    return redirect("/square/" + num)


@app.route("/square/<number>")
def square(number):
    number = int(number)
    squareNum = number*number
    return render_template("squareResult.html", result=squareNum)


app.run(port=3000)
