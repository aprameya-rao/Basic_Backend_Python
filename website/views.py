from flask import Blueprint

views=Blueprint('views',__name__)


@views.route('/') #for home page
def home():
    return "hqmepage"
