from flask import Flask, render_template, redirect, url_for, request, session, flash
import bcrypt
from pymongo import MongoClient


app = Flask(__name__)
app.secret_key = "your_secret_key"  # Replace with a strong secret key


# HOME PAGE --------------
@app.route('/')
def index():
    return render_template('index.html')


# ---------------- GOAT FARMING SERVICE PAGE ------------------
# -------------------------------------------------------------
@app.route('/goatfarming')
def goat_farming():
    return render_template('goat_farming.html')


# INNER PAGE TEMPLATE --------------------
@app.route('/login_goat_service', methods=['GET', 'POST'])
def login_goat_service():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        mongo_client = MongoClient("mongodb://localhost:27017/")
        db = mongo_client["farm_project"]
        users_collection = db["singup_goat_service"]

        user = users_collection.find_one({'email': email, 'password': password})

        if user:
            session['email'] = email
            return redirect(url_for('dashboard_goat_service'))
        else:
            flash('Invalid email or password')
            return redirect(url_for('home'))

    return render_template('login-goat-service.html')


@app.route('/signup_goat_service', methods=['GET', 'POST'])
def signup_goat_service():
    if request.method == 'POST':
        fullname = request.form['fullname']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        mongo_client = MongoClient("mongodb://localhost:27017/")
        db = mongo_client["farm_project"]
        users_collection = db["singup_goat_service"]
        print('I have connected to database')
        print('Here is the error')

        # Check if the passwords match
        if password != confirm_password:
            flash('Passwords do not match')
            return redirect(url_for('home'))
        print('There is the error')
        existing_user = users_collection.find_one({'email': email})

        if existing_user:
            print(existing_user)
            flash('Username already taken')
            return redirect(url_for('home'))
        else:
            users_collection.insert_one({'fullname': fullname, 'email': email, 'password': password, 'confirm_password': confirm_password})
            session['email'] = email
            return redirect(url_for('login_goat_service'))
    return render_template('signup-goat-service.html')


@app.route('/dashboard_goat_service')
def dashboard_goat_service():
    return render_template('dashboard_goat_service.html')
# ------------------------- END -------------------------------


# ABOUT US PAGE -----------------------------
@app.route('/about_us')
def about_us():
    return render_template('about-us.html')


if __name__ == '__main__':
    app.run(debug=True)
