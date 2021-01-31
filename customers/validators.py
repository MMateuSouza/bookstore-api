from re import search


def validate_email(email):
    result = search('^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$', email)
    return True if result else False
