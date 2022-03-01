# Code With Mosh Python Course: Python Basics

# type annotation(conflict)

#x: int = 1
# x = "Sample John"  # <<<<<this will throw a runtime error

# mutable

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
print(course.lstrip())  # deletes whitespaces at the beginning called left strip
print(course.rstrip())  # deletes whitespaces at the end called right strip

print(course.find("pro"))
print(course.replace("P", "-"))

print("Programming" in course)
print("Programming" not in course)
