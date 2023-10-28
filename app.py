from flask import Flask, render_template, redirect


app = Flask(__name__)


# HOME PAGE --------------
@app.route('/')
def index():
    return render_template('index.html')


# INNER PAGE TEMPLATE --------------------
@app.route('/innerpage')
def inner_page():
    return render_template('inner-page.html')


# ---------------- GOAT FARMING SERVICE PAGE ------------------
# -------------------------------------------------------------
@app.route('/goatfarming')
def goat_farming():
    return render_template('goat_farming.html')
# ------------------------- END -------------------------------


# ABOUT US PAGE -----------------------------
@app.route('/about_us')
def about_us():
    return render_template('about-us.html')


if __name__ == '__main__':
    app.run(debug=True)
