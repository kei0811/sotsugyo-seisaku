from flask import Flask, render_template, request, redirect, session
import sqlite3

app = Flask(__name__)

#秘密のカギ secret_keyの設定 sessionを使えるようにするために必要です
app.secret_key = 'sunabaco'



@app.route("/new", methods=["GET"])
def new_get():
    if "user_id" in session:
        return redirect("/main")
    else:     
        return render_template("new.html")



@app.route("/new", methods=["POST"])
def new_post():
    if "user_id" in session:
        return redirect("/main")
    else:    
        name = request.form.get("users_name")
        email = request.form.get("users_email")
        password = request.form.get("users_password")
        representative = request.form.get("users_representative")
        local = request.form.get("users_local")
        introduce = request.form.get("users_introduce")
        usimage = request.form.get("users_image")
        #flasktest.db接続
        conn = sqlite3.connect("20201209.db")
        #中を見れるようにする
        c = conn.cursor()
        #sqlを実行
        c.execute("insert into users values(null,?,?,?,?,?,?,?)",( name, email, password, representative, local, introduce, users_image ))
        #保存する
        conn.commit()
        #データベース読み込み終了
        c.close()
        return "登録完了"


if __name__ == "__main__":
    app.run(debug=True) 


# ここより下に書いても実行されないので注意