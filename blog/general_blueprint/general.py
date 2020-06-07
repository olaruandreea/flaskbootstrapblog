from flask import Blueprint, render_template, request
from flask_login import current_user


general_blueprint = Blueprint('general_blueprint', __name__,
                                                template_folder='templates',
                                                static_folder='static',
                                                static_url_path='/blog.general_blueprint.static')

@general_blueprint.route('/')
def home():
    return render_template("home.html")

@general_blueprint.errorhandler(404) 
def notFound(e): 
    return render_template("404.html") 


 