from flask import Flask,render_template,request,redirect,session
import sqlite3

app = Flask(__name__)



# Flask では標準で Flask.secret_key を設定すると、sessionを使うことができます。この時、Flask では session の内容を署名付きで Cookie に保存します。
app.secret_key = 'sunabakoza'

@app.route('/')
def login_get():
    return render_template('login.html')

# メインページへアクセス
@app.route("/main.html")
def move_main():
    return render_template("main.html")
# メインページから投稿画面へ
@app.route("/write.html", methods=["GET"])
def post():
    return render_template("write.html")
# データベースに情報追加
@app.route("/write.html",methods=["POST"])
def db_info():
    
    title = str(request.form.get("title_task"))
    intro = str(request.form.get("intro_task"))
    work  = str(request.form.get("title_task"))
    salary = str(request.form.get("salary_task"))
    target = str(request.form.get("target_task"))
    time = str(request.form.get("hours_task"))
    status = str(request.form.get("status_task"))
    walfare = str(request.form.get("walfare_task"))
    flow = str(request.form.get("flow_task"))
    sns_link = str(request.form.get("link_task"))
    conn = sqlite3.connect("20201209.db")
    c = conn.corsor()
    c.execute ("insert into job valuse(null, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"(title, intro, work, salary, target, time, status, walfare, flow, sns_link),)
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
