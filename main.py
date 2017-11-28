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



    return

@app.route('/')
def index():
    return render_template('signup.html', title="User Signup", heading="Signup")

app.run()