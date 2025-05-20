import random
hl = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
      'a', 'b', 'c', 'd', 'e', 'f']

hex2dec = random.choice(hl)
print('16進数: '+hex2dec)
print('10進数: '+str(int(hex2dec, 16)))
