from flask import Blueprint, render_template, request
from flask_login import current_user

faqs_blueprint = Blueprint('faqs_blueprint', __name__,
                                            template_folder='templates',
                                            static_folder='static',
                                            static_url_path='/website.blueprints.faqs_blueprint.static')

@faqs_blueprint.route("/faqs")
def faqs():
    return render_template("faqs.html")