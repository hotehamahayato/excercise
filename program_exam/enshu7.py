import random
target = random.randint(1, 100)
print(target)

if target%2 == 0:
    if target%10 == 0 or target%30 == 0:
        r = 'x'
    else:
        r = '◎'
elif target%3 == 0:
    if target%21 == 0:
        r = 'x'
    else:
        r = '◎'
elif target%35 != 0:
    r = '◎'
else:
    r = 'x'

print(r)
