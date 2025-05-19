def greet(name, time):
    if time == 'morning':
        return name+'さん、おはようございます。'
    elif time == 'noon':
        return name+'さん、こんにちは。'
    elif time == 'evening':
        return name+'さん、こんばんは。'
    else:
        None


print(greet('hotehama', 'noon'))
