# Sources:
# https://www.youtube.com/watch?v=DxI4jnb5m1Q
# https://www.youtube.com/watch?v=MwZwr5Tvyxo

from app import app
from flask import Flask, render_template, url_for, flash, redirect
from app.forms import LoginForm
from flask import request
from .forms import RegistrationForm, LoginForm
from .database import connect_to_database, execute_query
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


@app.route('/properties', methods=['POST', 'GET'])
def properties():
    if request.method == 'GET':
      print("Fetching properties.")
      db_connection = connect_to_database()
      query = "SELECT * FROM property"
      result = execute_query(db_connection, query).fetchall()
      print(result)
      return render_template("properties.html", properties=result)

    if request.method == 'POST':
      print("Adding new property")
      db_connection = connect_to_database()
      Street_Address = request.form['address']
      Unit_Number = request.form['unitnumber']
      Zip_Code = request.form['zipcode']
      Square_Feet = request.form['sf']
      Rooms = request.form['rooms']
      Bathrooms = request.form['bathrooms']
      Management_Fee = request.form['fee']
      Lease_ID = request.form['leaseid']
      print(Street_Address)

      query = "INSERT INTO property (Street_Address, Unit_Number, Zip_Code, Square_Feet, Rooms, Bathrooms, Management_Fee, Lease_ID) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
      data = (Street_Address, Unit_Number, Zip_Code, Square_Feet, Rooms, Bathrooms, Management_Fee, Lease_ID)
      execute_query(db_connection, query, data)
      print("Property added")
      query2 = "SELECT * FROM property"
      result = execute_query(db_connection, query2).fetchall()
      return render_template("properties.html", properties=result)


@app.route('/tenants')
def tenants():
    print("Fetching tenants.")
    db_connection = connect_to_database()
    query = "SELECT * FROM tenant"
    result = execute_query(db_connection, query).fetchall()
    print(result)
    return render_template("tenants.html", tenants=result)


@app.route('/owners')
def owners():
    print("Fetching owners.")
    db_connection = connect_to_database()
    query = "SELECT * FROM owner"
    result = execute_query(db_connection, query).fetchall()
    print(result)
    return render_template("owners.html", owners=result)


@app.route('/leases')
def leases():
    print("Fetching leases.")
    db_connection = connect_to_database()
    query = "SELECT * FROM lease"
    result = execute_query(db_connection, query).fetchall()
    print(result)
    return render_template("leases.html", leases=result)


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
