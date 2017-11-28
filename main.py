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

    redirect_args = "/"

    if (not username) or (username.strip() == ""):
        username_error = "Username cannot be left blank."
        redirect_args += "?username_error=" + username_error

    return redirect(redirect_args)

@app.route('/')
def index():
    # username = request.args.get("username")
    # email = request.args.get("email")

    username_error = request.args.get("username_error")
    # password_error = request.args.get("password_error")
    # verify_error = request.args.get("verify_error")
    # email_error = request.args.get("email_error")

    return render_template("signup.html", title="User Signup", heading="Signup", username_error=username_error and cgi.escape(username_error, quote=True))

app.run()
# , username_error=username_error  and cgi.escape(username_error, quote=True)
# email=email, username_error=username_error, password_error=password_error, verify_error=verify_error, email_error=email_error