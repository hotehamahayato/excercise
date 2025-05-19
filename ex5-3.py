def get_max(*args):
    if len(args) ==  0:
        return 0
    else:
        m = args[0]
        for i in args:
            if i > m:
                m = i
        return m


print(get_max(1,3,4,2))
print(get_max())
