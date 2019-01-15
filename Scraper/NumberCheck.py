def NumberCheck(entry):
    numbers = "1234567890"
    check = False
    for letter in entry:
        if letter in numbers:
            check = True
    return check
