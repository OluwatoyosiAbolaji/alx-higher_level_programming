#!/usr/bin/python3
number = 0
for number in range(100):
    if number == 99:
        print(f'{number:02d}')
    else:
        print(f'{number:02d},', end=' ')
