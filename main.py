from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True

@app.route('/signup', methods=['POST'])
def signup():
    # look inside the request to figure out what the user typed
    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']

    username_error = ""
    password_error = ""
    verify_error = ""
    email_error = ""

    if (not username) or (username.strip() == ""):
        username_error += "Username cannot be left blank."
    elif " " in username:
        username_error += "Username cannot contain a space character."
    elif len(username) < 3 or len(username) > 20:
        username_error += "Username must contain between 3-20 characters."
    
    if (not password) or (password.strip() == ""):
        password_error += "Password cannot be left blank."
    elif " " in password:
        password_error = "Password cannot contain a space character."
    elif len(password) < 3 or len(password) > 20:
        password_error += "Password must contain between 3-20 characters."

    if (not verify) or (verify.strip() == ""):
        verify_error += "Password verification cannot be left blank."
    elif password != verify:
        verify_error += "Passwords do not match."

    if email:
        if email.count("@") != 1 or email.count(".") != 1 or email.count(" ") > 0 or len(email) < 3 or len(email) > 20:
            email_error += "That's not a valid email."
        if len(email_error) != 0:
            email = ""
    
    if len(username_error) != 0:
        username = ""
    
    if len(username_error) != 0 or len(password_error) != 0 or len(verify_error) != 0 or len(email_error) != 0:
        return render_template("signup.html", title="User Signup", heading="Signup", 
            username_error=username_error and cgi.escape(username_error, quote=True),
            password_error=password_error and cgi.escape(password_error, quote=True), 
            verify_error=verify_error and cgi.escape(verify_error, quote=True), 
            email_error=email_error and cgi.escape(email_error, quote=True),
            username=username and cgi.escape(username, quote=True), 
            email=email and cgi.escape(email, quote=True))
    else:
        return render_template("welcome.html", title="Welcome", heading="Welcome, " + username + "!")

@app.route('/')
def index():
    username = request.args.get("username")
    email = request.args.get("email")

    username_error = request.args.get("username_error")
    password_error = request.args.get("password_error")
    verify_error = request.args.get("verify_error")
    email_error = request.args.get("email_error")

    return render_template("signup.html", title="User Signup", heading="Signup", 
            username_error=username_error and cgi.escape(username_error, quote=True),
            password_error=password_error and cgi.escape(password_error, quote=True), 
            verify_error=verify_error and cgi.escape(verify_error, quote=True), 
            email_error=email_error and cgi.escape(email_error, quote=True),
            username=username and cgi.escape(username, quote=True), 
            email=email and cgi.escape(email, quote=True))

app.run()