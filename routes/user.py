from flask import Blueprint, jsonify, render_template
from controller.user import signup_post

user_blueprint = Blueprint('user', __name__)

@user_blueprint.route('/signup/', methods=['GET'])
# Show signup page
def show_signup():
    return render_template('signup.html')

@user_blueprint.route('/signup/', methods=['POST'])
# Signup user
def process_signup():
    try:
        return signup_post()
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except KeyError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 400
