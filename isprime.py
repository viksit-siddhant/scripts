#!/usr/bin/env python3

import sys

orig_num = int(sys.argv[1])
num = orig_num
x = []
y = []
for i in range(2,int(num/2+1)):
    if num % i == 0:
        y.append(0)
        x.append(i)
    while num % i == 0:
        num /= i
        y[-1] += 1

print('1^1')
for j,num in enumerate(x):
    print(f'{num}^{y[j]}')
print(f'{orig_num}^1')

