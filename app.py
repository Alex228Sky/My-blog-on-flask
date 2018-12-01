from flask import Flask,render_template,request,session,logging,url_for,redirect
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session,sessionmaker

from passlib.hash import sha256_crypt
engine = create_engine("mysql+pymysql://root:password@localhost/register")
bd=scoped_session(sessionmaker(bind=engine))
app = Flask(__name__)


@app.route('/')
def home():
	return render_template('home.html')

#регистрация
@app.route('/register',method=["GET","POST"])
def register():
	if request.method == "POST":
		name = request.form.get("name")
		username = request.form.get("username")
		password = request.form.get("password")
		confirm = request.form.get("confirm")
		secure_password = sha256_crypt.encrypt(str(password))
		if password == confirm:

	return render_template('register.html')

#логин
@app.route('/login')
def login():
	return render_template('login.html')


if  __name__ == "__main__":
	app.run(debug=True)