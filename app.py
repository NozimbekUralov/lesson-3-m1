
from flask import Flask, render_template, request, redirect, url_for

from utils import validate_email, validate_password, validate_name, state
from db import DB

app = Flask(__name__)

@app.route('/')
def index():
    return render_template(
        'index.html',
        message=state['message']
        )

@app.route('/login', methods=['GET', 'POST'])
def login():
    if state['isAuth']:
        return redirect(url_for('index'))

    elif request.method == 'POST':
        form = request.form
        email = form['email']
        password = form['password']

        if validate_email(email) and validate_password(password):
            user = DB.find_user(email)
            if user:
                state['isAuth'] = True
                state['message'] = 'Wellcome'
                return redirect(url_for('index'))
            
            return render_template(
                'login.html',
                message='User not found'
                )
        
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if state['isAuth']:
        return redirect(url_for('index'))
    
    elif request.method == 'POST':
        form = request.form
        email = form['email']
        password = form['password']
        first_name = form['first_name']
        last_name = form['last_name']

        user = DB.find_user(email)

        if validate_email(email) and validate_password(password) and validate_name(first_name) and validate_name(last_name) and not user:
            DB.add_user(
                email,
                password,
                first_name,
                last_name
            )
            return redirect(url_for('login'))

        return render_template(
            'register.html',
            message='Invalid Credentials'
        )
    
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)