from flask import Flask,render_template,request,redirect,session
import sqlite3
import os
app = Flask(__name__)



# Flask では標準で Flask.secret_key を設定すると、sessionを使うことができます。この時、Flask では session の内容を署名付きで Cookie に保存します。
app.secret_key = 'sunabakoza'



@app.route('/')
def login_get():
    return render_template('login.html')



# メインページから投稿画面へ

@app.route("/write", methods=["GET"])
def post():
    if 'user_id' in session :
      user_id = session['user_id'] #flasktest.db接続
      return render_template("write.html")
    else:
        # ログインしてないと、ログイン画面に戻す
        return render_template("worker.html")

 # 連想配列を用いてpost画面に投稿
@app.route("/main")
def post_list():
    conn=sqlite3.connect("20201209.db")
    c=conn.cursor()
    c.execute("select * from job order by id desc")
    post_list=[]
    for row in c.fetchall():
        post_list.append({"id":row[0],"title":row[1],"intro":row[2],"work":row[3],"salary":row[4],"target":row[5],"location":row[6],"hours":row[7],"hoursf":row[8],"status":row[9],"holiday":row[10],"walfare":row[11],"flow":row[12],"link":row[13]})
    print(post_list)
    c.close()
    return render_template("main.html",tmp_post_list=post_list)




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





@app.route("/",methods=["POST"])
def login_post():
    name = request.form.get("member_name")
    password = request.form.get("member_pass")
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
        return redirect("/main")



@app.route("/logout")
def logout():
    session.pop("user_id",None)
    return redirect("/")

@app.route("/new", methods=["GET"])
def new_get():
       
    return render_template("new.html")



@app.route("/new", methods=["POST"])
def new_post():
   
    name = request.form.get("users_name")
    email = request.form.get("users_email")
    password = request.form.get("users_password")
    representative = request.form.get("users_representative")
    local = request.form.get("users_local")
    introduce = request.form.get("users_introduce")
    
    #flasktest.db接続
    conn = sqlite3.connect("20201209.db")
    #中を見れるようにする
    c = conn.cursor()
    #sqlを実行
    c.execute("insert into users values(null,?,?,?,?,?,?,?)",( name, email, password, representative, local, introduce, "no-img.gif" ))
    #保存する
    conn.commit()
    #データベース読み込み終了
    c.close()
    
    return render_template("new_after.html")


@app.route("/mypage")
def dbtest():
    if 'user_id' in session :
        user_id = session['user_id'] #flasktest.db接続
        conn = sqlite3.connect("20201209.db")
        #中を見れるようにする
        c = conn.cursor()
        #sqlを実行
        c.execute("select * from users where id = ?",(user_id,))
        #変数にSQLで取得した内容を格納する
        user_info = c.fetchone()
        #データベース読み込み終了
        print(str(user_info[7]))
        c.close()

        return render_template("mypage.html", tmp_user_info = user_info)
    else:
        # ログインしてないと、ログイン画面に戻す
        return render_template("/worker.html")
  
  
  

    
@app.route("/edit", methods=["GET"])
def edit_get():
    if 'user_id' in session :
        user_id = session['user_id']
        #flasktest.db接続
        conn = sqlite3.connect("20201209.db")
        #中を見れるようにする
        c = conn.cursor()
        #sqlを実行
        c.execute("select * from users where id = ?",(user_id,))
        #変数にSQLで取得した内容を格納する
        user_info = c.fetchone()
        #データベース読み込み終了
        c.close()

        return render_template("edit.html", tmp_user_info = user_info)
    else:
        return redirect("/")

@app.route("/edit", methods=["POST"])
def edit_post():
    if 'user_id' in session :
        user_id = session['user_id']

        name = request.form.get("users_name")
        email = request.form.get("users_email")
        password = request.form.get("users_password")
        representative = request.form.get("users_representative")
        local = request.form.get("users_local")
        introduce = request.form.get("users_introduce")
        # image = request.form.get("users_image")
        #flasktest.db接続 
        conn = sqlite3.connect("20201209.db")
        #中を見れるようにする
        c = conn.cursor()
        #sqlを実行
        c.execute("update users set name = ?, email = ?, password = ?,  representative = ?, local =?, introduce =? where id=?",( name, email, password, representative, local, introduce, user_id))
        #保存する
        conn.commit()
        #変数にSQLで取得した内容を格納する
        user_info = c.fetchone()
        #データベース読み込み終了
        c.close()

        return redirect("/mypage")
    else:
        return redirect("/")

@app.route('/upload', methods=["POST"])
def do_upload():
    # bbs.tplのinputタグ name="upload" をgetしてくる
    upload = request.files['upload']
    # uploadで取得したファイル名をlower()で全部小文字にして、ファイルの最後尾の拡張子が'.png', '.jpg', '.jpeg'ではない場合、returnさせる。
    if not upload.filename.lower().endswith(('.png', '.jpg', '.jpeg')):
        return 'png,jpg,jpeg形式のファイルを選択してください'
    
    # 下の def get_save_path()関数を使用して "./static/img/" パスを戻り値として取得する。
    save_path = get_save_path()
    # パスが取得できているか確認
    print(save_path)
    # ファイルネームをfilename変数に代入
    filename = upload.filename
    # 画像ファイルを./static/imgフォルダに保存。 os.path.join()は、パスとファイル名をつないで返してくれます。
    upload.save(os.path.join(save_path,filename))
    # ファイル名が取れることを確認、あとで使うよ
    print(filename)
    
    # アップロードしたユーザのIDを取得
    user_id = session['user_id']
    conn = sqlite3.connect('20201209.db')
    c = conn.cursor()
    # update文
    # 上記の filename 変数ここで使うよ
    c.execute("update users set image = ? where id  = ?", (filename, user_id))
    conn.commit()
    conn.close()

    return redirect ('/edit')

def get_save_path():
    path_dir = "./static/img"
    return path_dir



@app.route("/main#")
def mainpge():
    return render_template("login.html")




















































if __name__=="__main__":
    app.run(debug=True)

# ここより下に書いても実行されないので注意
