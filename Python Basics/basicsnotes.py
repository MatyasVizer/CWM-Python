# Code With Mosh Python Course: Python Basics

# type annotation(conflict)

# x: int = 1
# x = "Sample John"  # <<<<<this will throw a runtime error

# mutable

import math  # math is now an object
y = 1
print(id(y))
y = y + 1
print(id(y))

# immutable

z = [1, 2, 3]
print(id(z))
z.append(4)
print(id(z))


# 5: strings

course = "Python Course"
print(len(course))
print(course[0])
print(course[-1])
print(course[0:3])
print(course[:3])  # passes zero as start index on default
print(course[0:])  # passes end index on default
print(course[:])  # passes the defualt values


# 6: escape sequences

message = 'Python "Programming'
print(message)

message = "Python\"Programming"
print(message)

message = "Python\\Programming"
print(message)

message = "Python\nProgramming"
print(message)

message = """Python
Programming
"""
print(message)


# 7: formatted strings

first = "Matyas"
last = "Vizer"
full = f"{first} {last}"
full2 = f"{len(first)} {2 + 18}"
print(full)
print(full2)


# 8: useful string methods for string objects

print(course.upper())
print(course.lower())
print(course.title())

print(course.strip())  # deletes whitespaces
print(course.lstrip())  # deletes whitespaces at the beginning called left stri
print(course.rstrip())  # deletes whitespaces at the end called right strip

print(course.find("pro"))
print(course.replace("P", "-"))

print("Programming" in course)
print("Programming" not in course)

# 9: numbers

x1 = 10
x2 = 0b10
x3 = 0x12c
print(x1)
print(bin(x2))
print(hex(x3))

# a + bi
x4 = 1 + 2j
print(x4)


# 10: arithmetic operators

y1 = 10 + 3
y2 = 10 - 3
y3 = 10 * 3
y4 = 10 / 3
y5 = 10 // 3
y6 = 10 % 3
y7 = 10 ** 3

y8 = 0
y8 += 1

print(y1)
print(y2)
print(y3)
print(y4)
print(y5)
print(y6)
print(y7)
print(y8)

# 11: working with numbers


PI = -3.14  # markup for constant
print(round(PI))
print(abs(PI))
print(math.floor(PI))

# search python math module for more info

# 12: type conversion

# x = input("x: 3")
x = 3
print(int(x))
print(float(x))
print(bool(x))
# str(x)


# 13: conditional statements

age = 22
if age >= 18:
    print("Adult")
    print("Adult")
elif age >= 13:
    print("Teenager")
else:
    print("Child")

print("All done")


# 14: conditional operators

name = " "

if not name.strip():
    print("Name is empty")


age = 22
if age >= 18 and age < 65:
    print("Eligible")

# chaining comparison operators

age = 22
if 18 <= age < 65:
    print("Eligible")

# 15: ternary operators

message = "Eligible" if age >= 18 else "Not eligible"
print(message)

# 16: for loops

for x in "Python":
    print(x)

for x in ['a', 'b', 'c']:
    print(x)

for x in range(0, 10, 2):
    print(x)

print(type(range(5)))


# 17: for...else

names = ["John", "Mary"]
for name in names:
    if name.startswith("J"):
        print("Found")
        break
else:
    print("Not found")

# if the iteration completes without "break" then
# the else statement will be valid

# 18: while loops

guess = 0
answer = 5

while answer != guess:
    guess = int(input("Guess: "))
else:
    pass


# 19: functions

numberslist = [1, 2, 3]  # list
numberstuple = (1, 2, 3)  # tuple


def increment(number: int, by: int = 1) -> tuple:
    return (number, number + by)


print(increment(2, 3))
print(increment(2))


# 20: arguments xargs

def multiply(*list):
    total = 1
    for number in list:
        total *= number
    return total


print(multiply(2, 3, 4, 5))  # python packages multiple arguments into a tuple


# 21: arguments xxargs


def save_user(**user):
    print(user)
    print(user["name"])

# ^^^^^^this creates a dictionary which is similar to an object


save_user(id=1, name="admin")


# 22: scope
message = "a"


def greet():
    global message
    message = "b"


greet()
print(message)
