# 1: lists

from array import array
from collections import deque
letters = ["a", "b", "c"]
matrix = [[0, 1], [2, 3]]  # matrix, 2d list
zeros = [0] * 5
combined = zeros + letters
numbers = list(range(20))
chars = list("Hello World")

print(len(chars))
print(combined)
print(numbers)


# 2: accessing items

letters = ["a", "b", "c", "d"]
letters[0] = "A"

print(letters[-1])
print(letters[0:3])
print(letters[:3])
print(letters[::2])


numbers = list(range(20))
print(numbers[::2])  # even numbers
print(numbers[::-1])  # reverse order


# 3: list unpacking

numbers = [1, 2, 3, 4, 4, 4, 4, 4]
# first, second, third = numbers  # list unpacking, have to match
# the number of items in the list

first, *other, last = numbers  # list unpacking, have to match
# the number of items in the list

print(first, last)
print(other)

# list unpacking old
first = numbers[0]
second = numbers[1]
third = numbers[2]

# 4: looping over lists

letters = ["a", "b", "c"]
items = [0, "a"]
index, letter = items

for letter in enumerate(letters):  # old syntax
    print(letter[0], letter[1])

for index, letter in enumerate(letters):  # new syntax
    print(index, letter)

# 5: adding or removing items


letters = ["a", "b", "c"]

# Add

letters.append("d")
letters.insert(0, "-")
print(letters)

# Remove

letters.pop(0)
letters.remove("b")
print(letters)
del letters[0:2]
print(letters)
letters.clear()
print(letters)


# 6: finding items

letters = ["a", "b", "c", "d"]

print(letters.count("d"))

if "d" in letters:
    print(letters.index("d"))

# 7: sorting lists

numbers = [3, 51, 2, 8, 6]
# numbers.sort()
new_numbers = sorted(numbers, reverse=True)
print(numbers)
print(new_numbers)

items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]


def sort_item(item):
    return item[1]


items.sort(key=sort_item)
print(items)


# 8: lambda functions

items.sort(key=lambda item: item[1])
print(items)


# 9: map function

items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]

# old syntax

prices = []
for item in items:
    prices.append(item[1])

print(prices)


# new syntax

prices = list(map(lambda item: item[1], items))
print(prices)


# 10: filter function

filtered = []

x = list(filter(lambda item: item[1] >= 10, items))
print(x)


# 11: list comprehension

# they are the same

prices = list(map(lambda item: item[1], items))  # old
prices = [item[1] for item in items]  # new
print(prices)

filtered = list(filter(lambda item: item[1] >= 10, items))
filtered = [item for item in items if item[1] >= 10]
print(filtered)


# 12: zip function

list1 = [1, 2, 3]
list2 = [10, 20, 30]

print(list(zip(list1, list2)))
print(list(zip("abc", list1, list2)))


# 13: stacks

# LIFO Last In - First Out

browsing_session = []
browsing_session.append(1)
browsing_session.append(2)
browsing_session.append(3)
print(browsing_session)
last = browsing_session.pop()
print(last)
print("redirect", browsing_session[-1])
if not browsing_session:
    print("disable")

# 14: queues

# FIFO First In - First Out

queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)
queue.popleft()
print(queue)
if not queue:
    print("empty")


# 15: tuples

# tuple is a read-only object

point = (1, 2) + (3, 4)
print(point[1])
print(point[0:2])
if 10 in point:
    print("exists")

point = (1, 2) * 3
print(point)
point = tuple("Hello World")
print(point)

# tuples are great for preventing accidental object modifications

# 16: swapping variables

x = 10
y = 11

# we can swap it like that:

z = x
x = y
y = z

# but that's obsolete, here is the new

x, y = y, x

# 17: arrays

# need to import module: from array import array

# python 3 typecode!!!

# only use arrays if you are using a large sequence of numbers!!!
# else use tuples and lists

arraynumbers = array("i", [1, 2, 3])  # "i" is the type of the array!!!
arraynumbers.append(4)
arraynumbers.insert(2, 5)
arraynumbers.pop(4)
arraynumbers.remove(5)

# 18: sets

# collection with no duplicates

setofnumbers = [1, 1, 2, 3, 4]
first = set(setofnumbers)
second = {1, 5}  # we define sets with curly brackets
second.add(6)
second.remove(6)

print(first | second)  # certain types of unions of two sets
print(first & second)  # if both contains it
print(first - second)  # if only the first contains it
print(first ^ second)  # omits that are in the union

# we can not access it with indexes, for that we need a list

if 1 in first:
    print("yes")

# 19: dictionaries


# 20: dictionary comprehensions


# 21: generator expressions


# 22: unpacking operators
