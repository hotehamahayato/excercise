import random
l = []
s = set()

for i in range(1, 100):
    n = random.randint(1, 100)
    l.append(n)

print(l)

for i in l:
    s.add(i)

print(s)
