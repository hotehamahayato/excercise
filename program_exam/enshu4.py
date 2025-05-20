import random
import string

beforeChar = random.choice(string.ascii_letters)
print(beforeChar)

if beforeChar.isupper():
    print(beforeChar.lower())
elif beforeChar.islower():
    print(beforeChar.upper())
