from flask import Flask, flash, redirect, render_template, request, session, abort, url_for
import models as dbHandler
import os
app = Flask(__name__)
@app.route("/")
def home():
	if not session.get('logged_in'):
		return redirect(url_for('login'))
	else:
		 return redirect(url_for('chat'))#first page to display
@app.route("/chat")
def chat():
 return render_template('chat.html')
@app.route("/register",methods=['POST','GET'])
def register():
	if request.method=='POST':
   		username = request.form['username']
   		password1 = request.form['password']
        password2=request.form['pass']
        email=request.form['email']
        if password1==password2:
            dbHandler.insertUser(username, password1,email)
            return render_template('index.html')
   	else:
   		return render_template('register.html')

@app.route("/login",methods=['POST', 'GET'])
def login():
    
 if request.method=='POST':
        username = request.form['username']
        password = request.form['password']
        
        user = dbHandler.retrieveUsers()
        udic=dict( user)
        print udic
        if username not in udic.keys():
            print "no user"
            flash('user not found!')
        elif password==udic[username]:
            print "loggedin"
            session['logged_in'] = True
            session['username'] = username
        else:
            print"wrong pass"
            flash('wrong password!')
        return home()
 else:
        return render_template('index.html')
@app.route("/logout")
def logout():
	session.pop('logged_in',None)
	session.pop('username',None)
if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(port=8000,debug = True)
