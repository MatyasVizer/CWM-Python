# 7: cost of raising exceptions

from timeit import timeit

code1 = """
def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be 0 or less")
    return 10 / age


try:
    calculate_xfactor(-1)
except ValueError as error:
    pass
"""


code2 = """
def calculate_xfactor(age):
    if age <= 0:
        return None
    return 10 / age

xfactor = calculate_xfactor(-1)
if xfactor == None:
    pass
"""


print("First code: ", timeit(code1, number=100000))
print("Second code: ", timeit(code2, number=100000))
