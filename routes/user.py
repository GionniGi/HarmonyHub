from flask import Blueprint, jsonify, render_template
from controller.user import signup_post

bp = Blueprint('user', __name__)

@bp.route('/signup/', methods=['GET'])
# Show signup page
def show_signup():
    return render_template('signup.html')

@bp.route('/signup/', methods=['POST'])
# Signup user
def process_signup():
    try:
        return signup_post()
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except KeyError as e:
        return jsonify({"error": str(e)}), 400
    