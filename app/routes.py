# Sources:
# https://www.youtube.com/watch?v=DxI4jnb5m1Q
# https://www.youtube.com/watch?v=MwZwr5Tvyxo

from app import app
from flask import Flask, render_template, url_for, flash, redirect
from app.forms import LoginForm
from .forms import RegistrationForm, LoginForm
#from wtforms.widgets.html5 import NumberInput
#from wtforms.fields.html5 import DateField
#from wtforms.validators import DataRequired, Length, NumberRange, ValidationError, AnyOf, Optional

#app = Flask(__name__)

#app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfdj192ta234'

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    return render_template('index.html', title='Home', user=user)


# @app.route('/', methods=['GET'])
# def index():
#     return render_template("index.html")


@app.route('/properties')
def properties():
    return render_template("properties.html")


@app.route('/tenants')
def tenants():
    return render_template("tenants.html")


@app.route('/owners')
def owners():
    return render_template("owners.html")


@app.route('/leases')
def leases():
    return render_template("leases.html")


@app.route('/editproperty')
def editproperty():
    return render_template("editproperty.html")


@app.route('/register', methods=['GET', 'POST'])
def register():
        form = RegistrationForm()
        print('in register')
        if form.is_submitted():
            flash(f'Account created for {form.username.data}!', 'success')
            print('success')
            return redirect(url_for('index'))
        return render_template("register.html", title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.is_submitted():
        if form.username.data == 'admin' and form.password.data == 'toor':
            flash('You have been logged in.', 'success')
            return redirect(url_for('index'))
        else:
            flash('Login unsuccessful. Incorrect username or password', 'danger')
    return render_template("login.html", title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)
