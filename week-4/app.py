from flask import Flask, render_template, request, session, redirect, url_for
import os

app = Flask(__name__)
app.secret_key = os.urandom(12)
# app.config["PERMANENT_SESSION_LIFETIME"] = 60                         # seconds, 設置 session 的有效期

@app.route('/')
def index():
    if "account" in session:
        return redirect(url_for('member'))
    return render_template('index.html')

@app.route('/signup', methods=['POST'])
def signup():
    if request.form['account'] == 'test' and request.form['password'] == 'test':
        session['account'] = request.form['account']
        return redirect(url_for('member'))
    else:
        return redirect(url_for('error', message='帳號、或密碼輸入錯誤'))       # redirect to error page, and pass message as query string key

@app.route('/logout')
def logout():
    session.pop('account', None)
    return redirect(url_for('index'))

@app.route('/member')
def member():
    if "account" in session:
        return render_template('member.html')
    else:
        return redirect(url_for('index'))

@app.route('/error')
def error():
    message = request.args.get('message')                               # request.args.get('query_string_keyname', 0, type=int)
    return render_template('error.html', error_msg=message)

@app.route('/square', methods=['POST'])
def square():
    input = request.form['num']                                         # request.form.get('num'), 'num' is the name of input
    input = int(input)
    return redirect(url_for('calc_square', num=input))

@app.route('/square/<int:num>')
def calc_square(num):
    return render_template('square.html', result = num ** 2)

if __name__ == '__main__':
    app.run(debug=True, port=3000)