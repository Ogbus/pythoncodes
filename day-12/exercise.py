import math
import string
import random
# Writ a function which generates a six digit random_user_id.
# print(random())
# print(randint(3,9))

def random_user_id(stringLength = 6):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))
print(random_user_id())

multiple_variable = lambda a, b, c: a ** 2 - 3 * b + 4 * c
print(multiple_variable(5, 5, 3))