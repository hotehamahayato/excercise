import time
import random


def deco(func):
    def wrapper(*args, **kwargs):
        st = time.perf_counter()
        result = func(*args, **kwargs)
        et = time.perf_counter()
        dt = et - st
        print(str(dt))
        return result
    return wrapper


@deco
def hit_number(num):
    while True:
        rn = random.randint(1, 3000000)
        if rn == num:
            break
    return 'hit'


print(hit_number(100))
