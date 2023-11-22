from flask import request, Blueprint, jsonify, render_template
from utils import get_ip, calculate_average
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
            calculate_average(
                data.get('extroversion1', 0),
                data.get('extroversion2', 0),
                data.get('extroversion3', 0)
                ),
            calculate_average(
                data.get('friendliness1', 0),
                data.get('friendliness2', 0),
                data.get('friendliness3', 0)
                ),
            calculate_average(
                data.get('conscientiousness1', 0),
                data.get('conscientiousness2', 0),
                data.get('conscientiousness3', 0)
                ),
            calculate_average(
                data.get('openess1', 0),
                data.get('openess2', 0),
                data.get('openess3', 0)
                ),
            calculate_average(
                data.get('stability1', 0),
                data.get('stability2', 0),
                data.get('stability3', 0)
                ),
            ip_address
        )
        return jsonify(response), 200
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