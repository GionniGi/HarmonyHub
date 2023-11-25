from flask import request, Blueprint, jsonify, render_template
from controllers.user import signup_post

user_blueprint = Blueprint('user', __name__)

@user_blueprint.route('/signup/', methods=['GET', 'POST'])
def signup():
    """
    Handle user signup.

    GET: Return signup page.
    POST: Signup user.
    """
    if request.method == 'GET':
        return render_template('signup.html')
    try:
        user_post()
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except KeyError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@user_blueprint.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')