from flask import Blueprint, render_template, request

about_blueprint = Blueprint('about_blueprint', __name__, 
                                            template_folder='templates', 
                                            static_folder='static',
                                            static_url_path='/website.blueprints.about_blueprint.static')

@about_blueprint.route('/aboutme')
def aboutMe():
    return render_template('aboutme.html')
