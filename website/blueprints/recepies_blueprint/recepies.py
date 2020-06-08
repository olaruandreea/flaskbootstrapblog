from flask import Blueprint, render_template, request

recepies_blueprint = Blueprint('recepies_blueprint', __name__,
                                template_folder='templates', 
                                static_folder='static',
                                static_url_path='/website.blueprints.recepies_blueprint.static')

@recepies_blueprint.route('/recepies')
def recepies():
    return render_template("recepies.html") 
