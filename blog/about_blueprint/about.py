from flask import Blueprint, render_template, request

about_blueprint = Blueprint('about_blueprint', __name__, template_folder='templates')

@about_blueprint.route('/aboutme')
def aboutMe():
    return render_template('aboutme.html')
