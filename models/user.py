# User class
class User:
    def __init__(self, username, email, password, first_name, last_name, birth_date, description, extroversion, friendliness, conscientiousness, openness, emotional_stability):
        self.username = username
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.description = description
        self.ratings = {
            'extroversion': extroversion,
            'friendliness': friendliness,
            'emotionalStability': emotional_stability,
            'openness': openness,
            'conscientiousness': conscientiousness
        }