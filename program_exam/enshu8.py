import random
sd = random.randint(1, 31)
ed = random.randint(1, 31)

if sd == ed:
    sd = random.randint(1,31)
elif sd > ed:
    sd, ed = ed, sd

if (sd < 10 and ed < 10) or (15 < sd and 15 < ed):
    print(f'セール期間({sd}日～{ed}日)は改装工事の期間と被っていません。')
else:
    print(f'セール期間({sd}日～{ed}日)が改装工事の期間と被っています。')
