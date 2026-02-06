class WeakPasswordError(Exception):
    pass

def is_strong(password):
    special_chars = "!@#$%^&*-_+="

    if len(password) < 8:
        raise WeakPasswordError("Password must contain at least 8 characters")
    if not any(ch.isupper() for ch in password):
        raise WeakPasswordError("Password must contain at least one uppercase letter")
    if not any(ch.islower() for ch in password):
        raise WeakPasswordError("Password must contain at least one lowercase letter")
    if not any(ch.isdigit() for ch in password):
        raise WeakPasswordError("Password must contain at least one digit")
    if not any(ch in special_chars for ch in password):
        raise WeakPasswordError("Password must contain at least one special char (!@#$%^&*-_+=)")
    return True, "Password is strong!"


password = input("enterpassword")

try:
    result = is_strong(password)
    print(result)
except WeakPasswordError as e:
    print(False, e)














