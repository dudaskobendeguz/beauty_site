from flask import Flask, request, render_template, redirect, url_for
import bussines_logic
import data_manager
app = Flask(__name__)


@app.route('/')
def login():
    message = ''
    if request.args:
        message = 'Hibás felhasználónév'
    return render_template('login.html', message=message)


@app.route('/register', methods=['POST'])
@app.route('/registration')
def register_new_user():
    if request.method == 'POST':
        user = bussines_logic.register(request.form['email'])
        data_manager.login(user)
        return redirect('/main_page')
    return render_template('registration.html')


@app.route('/login', methods=['POST'])
def log_in():
    if request.method == "POST":
        user = data_manager.validate_login(request.form['username'])
        if user:
            return redirect('/main_page')
    return redirect('/?login=false')








@app.route('/main_page')
def main_page():
    user = data_manager.logged_in_user()
    if not user:
        return redirect('/')
    return render_template('main_page.html', user=user)


@app.route('/good-bye<username>')
def good_bye(username):
    booked_date = '2021.12.01'
    return render_template('good_bye.html', user=username, date=booked_date)


@app.route('/log-out')
def log_out():
    user = data_manager.logged_in_user()
    data_manager.logout()
    return redirect(f'/good-bye{user["username"]}')


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        debug=True,
        port=8000
    )