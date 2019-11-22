import os
from flask import Flask, flash, redirect, render_template, request, url_for, make_response, escape, session, abort
import pymysql

app = Flask(__name__)

app.secret_key = os.urandom(16)   
print(os.urandom(16))

conn = pymysql.connect(host='localhost', port=3306, user='root', password='mypassword', database='gjg_vef2_v7')
# https://pythonspot.com/login-authentication-with-flask/
@app.route('/')
def index():
    if not session.get('logged_in'):
        return render_template('index.tpl')
    else:
        return render_template('admin.tpl')

@app.route('/nyskra', methods=['GET', 'POST'])
def nyr():
    error = None
    if  request.method == 'POST':
        userDetails = request.form
        user = userDetails['user_name']
        email = userDetails['user_email']
        password = userDetails['user_password']
        try:        
            cur = conn.cursor()
            cur.execute("INSERT INTO gjg_vef2_v7.users(user_name, user_email, user_password) VALUES(%s, %s, %s)",(user, email, password))
            conn.commit()
            cur.close()
            flash('Nýskráning tókst! Skráðu þig inn')
            #return redirect('/index')
            return redirect(url_for('users')) 
        except pymysql.IntegrityError:
            error = 'Nýskráning tókst ekki'  

    return render_template('index.tpl', error=error)

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        user = request.form.get('user_name')
        psw = request.form.get('user_password')

        conn = pymysql.connect(host='localhost', port=3306, user='root', password='mypassword', database='gjg_vef2_v7')
        cur = conn.cursor()
        cur.execute("SELECT count(*) FROM gjg_vef2_v7.users where user_name=%s and user_password=%s",(user,psw))
        result = cur.fetchone() #fáum tuple -fetchone
        print(result)

    # er user og psw til í db?
        if result[0] == 1:
            cur.close()
            conn.close()
            flash('Innskráning tókst, ')
            session['logged_in'] = True
            return redirect(url_for('admin'))
        else:
            error = 'Innskráning mistókst - reyndu aftur'
    return render_template('index.tpl', error=error)

@app.route('/users')
def users():
    cur = conn.cursor()
    resultValue = cur.execute("SELECT user_name FROM gjg_vef2_v7.users")  # ná í user_name dálk
    if resultValue > 0:
        userDetails = cur.fetchall()
        return render_template('users.tpl',userDetails=userDetails)

@app.route('/admin')
def admin():
    if not session.get('logged_in'):
        return render_template('index.tpl')
    else:
        try:
            cur = conn.cursor()
            resultValue = cur.execute("SELECT * FROM gjg_vef2_v7.users")  # * = allir dálkar
            if  resultValue > 0:
                userDetails = cur.fetchall()
                flash('velkomin')
                return render_template('admin.tpl',userDetails=userDetails)
        except pymysql.IntegrityError:
            error = 'Þú hefur ekki aðgang að þessari síðu'  
        return render_template('index.tpl')


@app.route("/logout")
def logout():
    session['logged_in'] = False
    return render_template('index.tpl')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.tpl'), 404

@app.errorhandler(400)
def bad_request(error):
    return render_template('bad_request.tpl'), 400

@app.errorhandler(500)
def bad_post(error):
    return render_template('bad_post.tpl'), 500

if __name__ == '__main__':
    app.run(debug=True)
#    app.run()