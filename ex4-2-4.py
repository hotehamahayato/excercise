students_data = [
    {"name": "A", "math": 85, "english": 92, "science": 78},
    {"name": "B", "math": 70, "english": 81, "science": 88},
    {"name": "C", "math": 95, "english": 88, "science": 92},
    {"name": "D", "math": 60, "english": 75, "science": 70},
    {"name": "E", "math": 88, "english": 90, "science": 85},
]
# 1
n = 0
sum = 0
for i in students_data:
    sum += students_data[n].get("math")
    n += 1

avr = sum/n
print(avr)

# 2
n2 = 0
ss = 0  # 理科の点数
hs = 0  # 最高得点
for i in students_data:
    ss = students_data[n2].get("science")

    if ss > hs:
        hs = ss
        name = students_data[n2].get("name")

    n2 += 1

print('名前:' + name + ' | 点数:' + str(hs))

# 3
n3 = 0
sum2 = 0
for i in students_data:
    sum2 = (students_data[n3].get("math") + students_data[n3].get("english") +
            students_data[n3].get("science"))

    students_data[n3]['total'] = sum2

    n3 += 1

print(students_data)





