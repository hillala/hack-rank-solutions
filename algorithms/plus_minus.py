#!/bin/python

import sys


n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))
x1=0
x2=0
x3=0
for i in range(n):
    if arr[i]>0:
        x1+=1
    elif arr[i]<0:
        x2+=1
    else:
        x3+=1
        
print(x1/float(n))
print(x2/float(n))
print(x3/float(n))

