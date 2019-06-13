#!/bin/python

import sys


n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))
for p in range(len(arr)-1,-1,-1):
    print arr[p],