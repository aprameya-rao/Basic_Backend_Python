from flask import Blueprint,render_template  #to import templates need to import render_template

views=Blueprint('views',__name__)


@views.route('/') #for home page
def home():
    return render_template("home.html")
