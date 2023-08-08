#!/usr/bin/python3
number = 0
for number in range(100):
    if number == 99:
        print('{:02d}'.format(number))
    else:
        print('{:02d},'.format(number), end=' ')
