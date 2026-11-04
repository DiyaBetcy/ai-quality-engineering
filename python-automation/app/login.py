def validate_login(username, password):
    if not username or not password:
        return False

    if username == "admin":
        return True

    return False