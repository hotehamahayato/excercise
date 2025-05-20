emp = ''
print(emp, end='\t')
for r in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
    print(r, end='\t')
print()
for i in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
    print(i, end='\t')
    for j in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        print(i*j, end='\t')
    print()
