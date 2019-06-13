#!/bin/python

import sys


n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))
while len(arr)>0:
    print(len(arr))
    num=min(arr)
    arr=[i-num for i in arr]
    arr=[i for i in arr if i>0]