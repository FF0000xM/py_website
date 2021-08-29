from  flask import Blueprint

auth = Blueprint('auth', __name__)

@auth.route('/in')
def in():
    return "<h2> Passcode? </h2>"

@auth.route('/out')
def out():
    return "<h2> Bye! </h2>"

@auth.route('/new-code')
def new_code():
    return "<h2> New Code. </h2>"
