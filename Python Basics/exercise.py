def fizz_buzz(input):
    message = ""
    if input % 3 == 0 and input % 5 != 0:
        message = "fizz"
        return message
    elif input % 5 == 0 and input % 3 != 0:
        message = "buzz"
        return message
    elif input % 3 == 0 and input % 5 == 0:
        message = "fizzbuzz"
        return message
    else:
        return input


print(fizz_buzz(33))
