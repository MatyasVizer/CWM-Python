# 1: lists

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
