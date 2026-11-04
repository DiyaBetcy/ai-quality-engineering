def validate_password(password):
    if len(password) < 5 or len(password) > 10:
        return False

    return True