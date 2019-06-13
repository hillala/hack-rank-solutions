#!/bin/python

import sys


n = int(raw_input().strip())
calories = map(int, raw_input().strip().split(' '))
# your code goes here
calories.sort()
sum=0
for i in range(n-1,-1,-1):
    sum=sum+(calories[i]*(2**(n-i-1)))
    
print(sum)