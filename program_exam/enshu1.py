import random
nenrei = random.randint(0, 100)
if nenrei < 20:
    print('未成年です。\n地方自治体によっては医療費が￥200のところも。')
elif 19 < nenrei < 60:
    print('成年です。\n飲酒・喫煙は控えめに。')
else:
    print('定年後も元気１００％で過ごしてください。')
