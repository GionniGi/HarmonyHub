from flask import request, Blueprint, jsonify, render_template
from utils import get_ip
from models.user.user import User

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
        ip_address = get_ip(request)
        data = request.json
        if not data:
            return jsonify({'error': 'No data provided'}), 400
        ip_address = get_ip(request)

        response = User().signup(
            data.get('username', ''),
            data.get('email', ''),
            data.get('password', ''),
            data.get('confirm_password', ''),
            data.get('first_name', ''),
            data.get('last_name', ''),
            data.get('birth_date', ''),
            data.get('description', ''),
            data.get('extroversion', 0),
            data.get('friendliness', 0),
            data.get('emotional_stability', 0),
            data.get('openness', 0),
            data.get('conscientiousness', 0),
            ip_address
        )
        return jsonify({"message": response}), 200
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