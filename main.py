# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from flask import Flask, render_template, request, flash

import utils
from forms import ContactUs

import yagmail as yagmail
import os

app = Flask(__name__)
app.debug = True
app.secret_key = os.urandom(12)
#app.secret_key = 'super secret key'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/register', methods=('GET', 'POST'))
def register():
    try:
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            email = request.form['email']

            if not utils.isEmailValid(email):
                error = "El email no es valido"
                flash(error)
                return render_template('register.html')

            if not utils.isUsernameValid(username):
                error = "El usuario no es valido"
                flash(error)
                return render_template('register.html')

            if not utils.isPasswordValid(password):
                error = "El password no es valido"
                flash(error)
                return render_template('register.html')

            yag = yagmail.SMTP('mintic202221@gmail.com', 'Mintic2022')
            yag.send(to=email,subject='Activa tu cuenta',
                     contents='Bienvenido al portal de Registro de Vacunación usa este link para activar tu cuenta')

            flash("Revisa tu correo para activar tu cuenta")
            return render_template('login.html')
        return render_template('register.html')
    except Exception as e:
        return render_template('register.html')


@app.route('/contactUs', methods=['GET', 'POST'])
def contactUs():
    form = ContactUs()
    return render_template('contactUs.html', form=form)
