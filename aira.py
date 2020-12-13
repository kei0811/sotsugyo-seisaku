from flask import Flask, render_template, request, redirect, session
import sqlite3

app = Flask(__name__)

# Flask では標準で Flask.secret_key を設定すると、sessionを使うことができます。この時、Flask では session の内容を署名付きで Cookie に保存します。
app.secret_key = 'sunabaco'

@app.route("/new")
def new():
    #flasktest.db接続
    conn = sqlite3.connect("20201209.db")
    #中を見れるようにする
    c = conn.cursor()
    #sqlを実行
    c.execute("init name, email, address from users where id = 1")
    #変数にSQLで取得した内容を格納する
    user_info = c.fetchone()
    #データベース読み込み終了
    c.close()

    return render_template("new.html",)








if __name__=="__main__":
    app.run(debug=True)

# ここより下に書いても実行されないので注意