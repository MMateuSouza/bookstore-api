def validate_isbn(isbn):
    is_valid = False

    if len(isbn) == 10:
        sequency = [(int(isbn[i]) * (i + 1)) for i in range(len(isbn[0:9]))]
        sum_ = sum(sequency)
        verifying_digit = str(sum_ % 11)
        if verifying_digit == '10':
            verifying_digit = 'X'
        is_valid = True if verifying_digit == isbn[-1].upper() else False
    elif len(isbn) == 13:
        sequency = [(int(isbn[i])) if i % 2 == 0 else (3 * int(isbn[i])) for i in range(len(isbn[0:12]))]
        sum_ = sum(sequency)
        verifying_digit = str(10 - (sum_ % 10))
        if verifying_digit == '10':
            verifying_digit = '0'
        is_valid = True if verifying_digit == isbn[-1] else False
    return is_valid
