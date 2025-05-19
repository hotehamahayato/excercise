# 1
def square(i):
    return i**2


print(square(2))
print(square(3))

# 2
def mul(x, *args):
    result = x
    for y in args:
        result *= y
    return result


print(mul(1, 2))
print(mul(2, 4, 6))
print(mul(3, 5, 7, 11))

# 3
def power(a):
    return lambda b: b**a


power3 = power(3)
power4 = power(4)

print(power3(2))
print(power4(3))

# 4
sum = 0
while True:
    try:
        en = input('Please input number:')
        n = int(en)
        psum = sum
        sum += n
        print(str(psum) + ' + ' + en + ' => ' + str(sum))
    except ValueError as ex:
        print('Not a number is inputted. Program exit.')
        break



