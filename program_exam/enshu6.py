import random
a = random.randint(1, 1000)
b = random.randint(1, 1000)

if a < b:
    a, b = b, a

print(a, b)

while True:
    if a % b == 0:
        break
    elif a % b != 0:
        r = a % b
        a = b
        b = r

print('最大公約数', +b)
