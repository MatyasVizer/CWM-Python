# 1: exceptions

# numbers = [1, 2]
# print(numbers[3]) incorrect

# age = int(input("Age: "))

# if you input anythin other than int, it will throw an error

# 2: handling exceptions

try:
    age = int(input("Age: "))
except ValueError as error:
    print("You didn't enter a valid age! Try again!")
    print(error)
    print(type(error))
else:
    print("No exceptions were thrown.")
    print("Execution continues...")


# 3: handling different exceptions

# 1:

try:
    age = int(input("Age: "))
    xfactor = 10 / age
except ValueError:
    print("You didn't enter a valid age! Try again!")
except ZeroDivisionError:
    print("Age cannot be zero!")
else:
    print("No exceptions were thrown.")

# 2:

try:
    age = int(input("Age: "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid age! Try again!")
else:
    print("No exceptions were thrown.")

# 4: cleaning up

try:
    file = open("app.py")
    age = int(input("Age: "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid age! Try again!")
else:
    print("No exceptions were thrown.")
finally:  # always executes at the end, use it to release external resources
    file.close()

# 5: the with statement

try:
    with open("app.py") as file, open("another.txt") as target:
        print("File opened")  # with statement automatically releases resources
        file.__exit__  # context management protocol
    age = int(input("Age: "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid age! Try again!")
else:
    print("No exceptions were thrown.")


# 6: raising exceptions

def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be 0 or less")
    return 10 / age


try:
    calculate_xfactor(-1)
except ValueError as error:
    print(error)
