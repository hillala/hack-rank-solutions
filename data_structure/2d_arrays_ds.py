#!/bin/python

import sys


arr = []
for arr_i in xrange(6):
    arr_temp = map(int,raw_input().strip().split(' '))
    arr.append(arr_temp)
s=-100
for i in range(0,4):
    for j in range(0,4):
        l=[k[j:3+j] for k in arr[i:3+i]]
        l[1][0]=0
        l[1][2]=0
        if sum(map(sum,l))>s:
            s=sum(map(sum,l))
print(s)