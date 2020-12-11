from flask import Flask,render_template,request,redirect,session
import sqlite3

app = Flask(__name__)

# Flask では標準で Flask.secret_key を設定すると、sessionを使うことができます。この時、Flask では session の内容を署名付きで Cookie に保存します。
app.secret_key = 'sunabakoza'

@app.route('/')
def login():
    return render_template('login.html')






































if __name__=="__main__":
    app.run(debug=True)

# ここより下に書いても実行されないので注意