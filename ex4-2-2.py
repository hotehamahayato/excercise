import random
l = []
l2 = []

for i in range(1, 100):
    n = random.randint(1, 100)
    l.append(n)

print(l)

for i in l:
    if i not in l2:
        l2.append(i)

print(l2)
