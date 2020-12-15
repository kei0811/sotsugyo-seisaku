from flask import Flask,render_template,request,redirect,session
import sqlite3

app = Flask(__name__)



# Flask では標準で Flask.secret_key を設定すると、sessionを使うことができます。この時、Flask では session の内容を署名付きで Cookie に保存します。
app.secret_key = 'sunabakoza'

@app.route('/')
def login_get():
    return render_template('login.html')

# メインページへアクセス
@app.route("/retrn")
def move_main():
    return render_template("main.html")


# 連想配列を用いてpost画面に投稿
@app.route("/main")
def post_list():
    conn=sqlite3.connect("20201209.db")
    c=conn.cursor()
    c.execute("select * from job")
    post_list=[]
    for row in c.fetchall():
        post_list.append({"id":[0],"title":[1],"intro":[2],"work":[3],"salary":[4],"target":[5],"location":[6],"hours":[7],"hoursf":[8],"status":[9],"holiday":[10],"walfare":[11],"flow":[12],"link":[13]})
    print(post_list)
    c.close()
    return render_template("main.html",temp_post_list=post_list)
    


# メインページから投稿画面へ
@app.route("/write", methods=["GET"])
def post():
    return render_template("write.html")

@app.route("/main")
def return_home():
    return render_template("main.html")




# データベースに情報追加
@app.route("/write",methods=["POST"])
def db_info():
    title = request.form.get("title_task")
    intro = request.form.get("intro_task")
    work = request.form.get("work_task")
    salary = request.form.get("salary_task")
    target = request.form.get("target_task")
    location = request.form.get("location_task")
    hours = request.form.get("hours_task")
    hoursf =request.form.get("hoursf_task")
    satus = request.form.get("status_task")
    holiday = request.form.get("holiday_task")
    walfare = request.form.get("walfare_task")
    flow = request.form.get("flow_task")
    link = request.form.get("link_task") 
    
    conn = sqlite3.connect("20201209.db")
    c = conn.cursor()
    c.execute ("insert into job values(null,?,?,?,?,?,?,?,?,?,?,?,?,?)",(title, intro, work, salary, target, location, hours, hoursf, satus, holiday,  walfare, flow, link))
    conn.commit()
    c.close()
    return render_template("post_after.html")



@app.route("/login",methods=["POST"])
def login_post():
    name = request.form.get("member_name")
    password = request.form.get("member_pass")
    # flasktest.db接続
    conn=sqlite3.connect("20201209.db")
    # 中を見れるようにする
    c=conn.cursor()
    # SQLを実行
    c.execute("select id from users where name=? and password=?",(name,password))
    user_id = c.fetchone()
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
