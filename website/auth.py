from flask import Blueprint
auth = Blueprint('auth',__name__)

@auth.route('/login')
def login():
    return "<p>login</p>"

@auth.route('/logout')
def logout():
    return "<p>logout</p>"

@auth.route('/sign-up')
def sign_in():
    return "<p>sign up</p>"