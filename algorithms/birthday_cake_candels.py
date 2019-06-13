#!/bin/python

import sys

def birthdayCakeCandles(n, ar):
    # Complete this function
    num=max(ar)
    x1=0
    for n in range(n):
        if ar[n]==num:
            x1+=1
    return x1

n = int(raw_input().strip())
ar = map(int, raw_input().strip().split(' '))
result = birthdayCakeCandles(n, ar)
print(result)
