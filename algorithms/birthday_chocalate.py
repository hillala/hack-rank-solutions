#!/bin/python

import sys

def solve(n, s, d, m):
    # Complete this function
    counter=0
    for i in range(n-m+1):
        if sum(s[i:i+m])==d:
            counter=counter+1
    return counter
n = int(raw_input().strip())
s = map(int, raw_input().strip().split(' '))
d, m = raw_input().strip().split(' ')
d, m = [int(d), int(m)]
result = solve(n, s, d, m)
print(result)
