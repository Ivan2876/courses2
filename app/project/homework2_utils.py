import re
def is_password_strong(password: str) -> bool:
    if len(password) < 8:
        return False
    if ' ' in password:
        return False
    if not re.search(r'[a-zA-Zа-яА-ЯіІїЇєЄґҐ]', password):
        return False
    if not re.search(r'\d', password):
        return False
    return True
