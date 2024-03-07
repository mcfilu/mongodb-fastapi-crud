from schemas.users import User


def create_user_inst(file):
    user_instance = User(first_name=file['first_name'], last_name=file['last_name'], occupancy=file['ocupation'], experience_years=file['experience_years'])
    return user_instance