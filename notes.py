# Code With Mosh Python Course: Python Basics

# type annotation(conflict)

x: int = 1
x = "Sample John"  # <<<<<this will throw a runtime error

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


# strings

course = "Python Course"
print(len(course))
print(course[0])
print(course[-1])
print(course[0:3])
print(course[:3])  # passes zero as start index on default
print(course[0:])  # passes end index on default
print(course[:])  # passes the defualt values
