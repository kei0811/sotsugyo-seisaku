from flask import Flask,render_template,request,redirect,session
import sqlite3

app = Flask(__name__)



# Flask では標準で Flask.secret_key を設定すると、sessionを使うことができます。この時、Flask では session の内容を署名付きで Cookie に保存します。
app.secret_key = 'sunabakoza'

@app.route('/login')
def login_get():
    return render_template('login.html')
# メインページへアクセス
@app.route("/main.html")
def move_main():
    return render_template("main.html")
# メインページから投稿画面へ
@app.route("/write.html")
def post():
    return render_template("write.html")
# データベースに情報追加
@app.route("/write.html",methods=["POST"])
def db_info():
    task = request.form.get("title_task", "intro_task", "work_task", "salary_task", "target_task", "location_task", "hours_task", "status_task", "holiday_task", "walfare_task", "flow_task", "link_task")
    conn = sqlite3.connect("20201209.db")
    c = conn.corsor()
    c.execute ("insert into job valuse(null, ?, ?, ?, ?, ?, ?, ?, ?, ?,  ?, ?, ?)")
    conn.commit()
    c.close()
    return"投稿されました"
    








@app.route("/login",methods=["POST"])
def login_post():
    name=request.form.get("member_name")
    password=request.form.get("member_pass")
    # flasktest.db接続
    conn=sqlite3.connect("20201209.db")
    # 中を見れるようにする
    c=conn.cursor()
    # SQLを実行
    c.execute("select id from users where name=? and password=?",(name,password))
    user_id=c.fetchone()
    conn.close()

    # user_id が NULL(PythonではNone)じゃなければログイン成功
    if user_id is None:
        # ログイン失敗すると、ログイン画面に戻す
        return render_template("login.html")
    else:
        session['user_id'] = user_id[0]
        return redirect("/main.html")






















































if __name__=="__main__":
    app.run(debug=True)

# ここより下に書いても実行されないので注意
