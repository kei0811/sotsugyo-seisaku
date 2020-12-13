from flask import Flask,render_template,request,redirect,session
import sqlite3

app = Flask(__name__)

# Flask では標準で Flask.secret_key を設定すると、sessionを使うことができます。この時、Flask では session の内容を署名付きで Cookie に保存します。
app.secret_key = 'sunabakoza'

@app.route('/login')
def login_get():
    return render_template('login.html')



@app.route("/login",methods=["POST"])
def login_post():
    name=request.form.get("member_name")
    password=request.form.get("member_pass")
    # flasktest.db接続
    conn=sqlite3.connect("20201209.db")
    # 中を見れるようにする
    c=conn.cursor()
    # SQLを実行
    c.execute("select id from users where name=? and pass=?",(name,password))
    user_id=c.fetchone()
    user_id=user_id[0]
    # データベース接続終了
    c.close()

    if user_id is None:#アカウント名、パスワードが一致しなかったとき
        return render_template("login.html")
    else:#アカウント名、パスワードが一致したとき
        session["user_id"]=user_id #sessionに格納
        return redirect("/main")
        # リンク先要指定


































if __name__=="__main__":
    app.run(debug=True)

# ここより下に書いても実行されないので注意