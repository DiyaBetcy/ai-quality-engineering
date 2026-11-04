def validate_login(username, password):
    if not username or not password:
        return False

    if username == "admin" and password == "12345":
        return True

    return False