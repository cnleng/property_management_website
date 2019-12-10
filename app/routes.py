# Sources:
# https://www.youtube.com/watch?v=DxI4jnb5m1Q
# https://www.youtube.com/watch?v=MwZwr5Tvyxo

from app import app
from flask import Flask, render_template, url_for, flash, redirect
from app.forms import LoginForm
from flask import request
from .forms import RegistrationForm, LoginForm
from .database import connect_to_database, execute_query
from wtforms.widgets.html5 import NumberInput
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired, Length, NumberRange, ValidationError, AnyOf, Optional
import os

#app = Flask(__name__)

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

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


@app.route('/tenants', methods=['POST', 'GET'])
def tenants():
    if request.method == 'GET':
      print("Fetching tenants.")
      db_connection = connect_to_database()
      query = "SELECT * FROM tenant"
      result = execute_query(db_connection, query).fetchall()
      print(result)
      return render_template("tenants.html", tenants=result)

    if request.method == 'POST':
      print("Adding new tenant.")
      db_connection = connect_to_database()
      Property_ID = request.form['propertyid']
      Lease_ID = request.form['leaseid']
      Name = request.form['tenantname']
      Credit_Score = request.form['credit']
      Social_Security = request.form['social']
      Date_Of_Birth = request.form['dob']
      print(Name)

      query = "INSERT INTO tenant (Property_ID, Lease_ID, Name, Credit_Score, Social_Security, Date_Of_Birth) VALUES (%s, %s, %s, %s, %s, %s)"
      data = (Property_ID, Lease_ID, Name, Credit_Score, Social_Security, Date_Of_Birth)
      execute_query(db_connection, query, data)
      print("Tenant added")
      query2 = "SELECT * FROM tenant"
      result = execute_query(db_connection, query2).fetchall()
      return render_template("tenants.html", tenants=result)


@app.route('/owners', methods=['POST', 'GET'])
def owners():
    if request.method == 'GET':
      print("Fetching owners.")
      db_connection = connect_to_database()
      query = "SELECT * FROM owner"
      result = execute_query(db_connection, query).fetchall()
      print(result)
      return render_template("owners.html", owners=result)

    if request.method == 'POST':
      print("Adding new owner")
      db_connection = connect_to_database()
      Number_Of_Properties = request.form['numproperties']
      Name = request.form['ownername']
      print(Name)

      query = "INSERT INTO owner (Number_Of_Properties, Name) VALUES (%s, %s)"
      data = (Number_Of_Properties, Name)
      execute_query(db_connection, query, data)
      print("Owner added")
      query2 = "SELECT * FROM owner"
      result = execute_query(db_connection, query2).fetchall()
      print(result)
      return render_template("owners.html", owners=result)


@app.route('/leases', methods=['POST', 'GET'])
def leases():
    if request.method == 'GET':
      print("Fetching leases.")
      db_connection = connect_to_database()
      query = "SELECT * FROM lease"
      result = execute_query(db_connection, query).fetchall()
      print(result)
      return render_template("leases.html", leases=result)

    if request.method == 'POST':
      print("Adding new lease")
      db_connection = connect_to_database()
      End_Date = request.form['enddate']
      Length_Of_Lease = request.form['length']
      Rent = request.form['rent']
      
      query = "INSERT INTO lease (End_Date, Length_Of_Lease, Rent) VALUES (%s, %s, %s)"
      data = (End_Date, Length_Of_Lease, Rent)
      execute_query(db_connection, query, data)
      print("Lease added")
      query2 = "SELECT * FROM lease"
      result = execute_query(db_connection, query2).fetchall()
      print(result)
      return render_template("leases.html", leases=result)


@app.route('/editproperty/<Property_ID>', methods=['POST', 'GET'])
def editproperty(Property_ID):
    print("Editing property")
    db_connection = connect_to_database()

    if request.method == 'GET':
      query = 'SELECT Property_ID, Street_Address, Unit_Number, Zip_Code, Square_Feet, Rooms, Bathrooms, Management_Fee, Lease_ID from property WHERE Property_ID = %s' % (Property_ID)
      result = execute_query(db_connection, query).fetchone()
      print(result)
      return render_template("editproperty.html", properties=result)

    if request.method == 'POST':
      print("Updating property...")
      Street_Address = request.form['address']
      Unit_Number = request.form['unitnumber']
      Zip_Code = request.form['zipcode']
      Square_Feet = request.form['sf']
      Rooms = request.form['rooms']
      Bathrooms = request.form['bathrooms']
      Management_Fee = request.form['fee']
      Lease_ID = request.form['leaseid']

      print(request.form)
      query = 'UPDATE property SET Street_Address = %s, Unit_Number = %s, Zip_Code = %s, Square_Feet = %s, Rooms = %s, Bathrooms = %s, Management_Fee = %s, Lease_ID = %s WHERE Property_ID = %s'
      data = (Street_Address, Unit_Number, Zip_Code, Square_Feet, Rooms, Bathrooms, Management_Fee, Lease_ID, Property_ID)
      result = execute_query(db_connection, query, data)

      return redirect('/properties')



@app.route('/edittenant/<Tenant_ID>', methods=['POST', 'GET'])
def edittenant(Tenant_ID):
    print("Editing tenant")
    db_connection = connect_to_database()

    if request.method == 'GET':
      query = 'SELECT Tenant_ID, Property_ID, Lease_ID, Name, Credit_Score, Social_Security, Date_Of_Birth from tenant WHERE Tenant_ID = %s' % (Tenant_ID)
      result = execute_query(db_connection, query).fetchone()
      print(result)
      return render_template("edittenant.html", tenants=result)

    if request.method == 'POST':
      print("Updating tenant...")
      Property_ID = request.form['property_id']
      Lease_ID = request.form['lease_id']
      Name = request.form['name']
      Credit_Score = request.form['credit_score']
      Social_Security = request.form['social_security']
      Date_Of_Birth = request.form['dob']

      print(request.form)
      query = 'UPDATE tenant SET Property_ID = %s, Lease_ID = %s, Name = %s, Credit_Score = %s, Social_Security = %s, Date_Of_Birth = %s WHERE Tenant_ID = %s'
      data = (Property_ID, Lease_ID, Name, Credit_Score, Social_Security, Date_Of_Birth, Tenant_ID)
      result = execute_query(db_connection, query, data)
      return redirect('/tenants')


@app.route('/editowner/<Owner_ID>', methods=['POST', 'GET'])
def editowner(Owner_ID):
    print("Editing owner.")
    db_connection = connect_to_database()

    if request.method == 'GET':
      query = 'SELECT Owner_ID, Number_Of_Properties, Name FROM owner WHERE Owner_ID =%s' % (Owner_ID)
      result = execute_query(db_connection, query).fetchone()
      print(result)
      return render_template('editowner.html', owners=result)

    if request.method == 'POST':
      print('Updating owner...')
      Number_Of_Properties = request.form['number']
      Name = request.form['name']

      print(request.form)
      query = 'UPDATE owner SET Number_Of_Properties = %s, Name = %s WHERE Owner_ID = %s'
      data = (Number_Of_Properties, Name, Owner_ID)
      result = execute_query(db_connection, query, data)
      return redirect('/owners')






@app.route('/deleteproperty/<Property_ID>')
def deleteproperty(Property_ID):
    print("Deleting property.")
    db_connection = connect_to_database()
    query = "DELETE FROM property WHERE Property_ID = %s"
    data = (Property_ID, )

    execute_query(db_connection, query, data)
    query2 = "SELECT * FROM property"
    result = execute_query(db_connection, query2).fetchall()
    print(result)
    return render_template("properties.html", properties=result)


@app.route('/deletetenant/<Tenant_ID>')
def deletetenant(Tenant_ID):
    print("Deleting tenant.")
    db_connection = connect_to_database()
    query = "DELETE FROM tenant WHERE Tenant_ID = %s"
    data = (Tenant_ID, )

    execute_query(db_connection, query, data)
    query2 = "SELECT * FROM tenant"
    result = execute_query(db_connection, query2).fetchall()
    print(result)
    return render_template("tenants.html", tenants=result)


@app.route('/deleteowner/<Owner_ID>')
def deleteowner(Owner_ID):
    print("Deleting owner.")
    db_connection = connect_to_database()
    query = "DELETE FROM owner WHERE Owner_ID = %s"
    data = (Owner_ID, )

    execute_query(db_connection, query, data)
    query2 = "SELECT * FROM owner"
    result = execute_query(db_connection, query2).fetchall()
    print(result)
    return render_template("owners.html", owners=result)    


@app.route('/deletelease/<Lease_ID>')
def deletelease(Lease_ID):
    print("Deleting lease.")
    db_connection = connect_to_database()
    query = "DELETE FROM lease WHERE Lease_ID = %s"
    data = (Lease_ID, )

    execute_query(db_connection, query, data)
    query2 = "SELECT * FROM lease"
    result = execute_query(db_connection, query2).fetchall()
    print(result)
    return render_template("leases.html", leases=result)


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
