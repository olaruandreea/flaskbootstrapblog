from flask import Blueprint, render_template, request
from flask_login import current_user
from werkzeug.exceptions import HTTPException
from flask import Flask, current_app


notfound_blueprint = Blueprint('notfound_blueprint', __name__,
                                                template_folder='templates',
                                                static_folder='static',
                                                static_url_path='/website.blueprints.notfound_blueprint.static')

@current_app.errorhandler(404) 
def notFound(e): 
    return render_template("404.html") 