#!/bin/python

import sys

def lonelyinteger(a):
    # Complete this function
    l=list(set(a))
    for k in l:
        n=len([j for j in a if j==k])
        if n==1:
            break
    return k
n = int(raw_input().strip())
a = map(int, raw_input().strip().split(' '))
result = lonelyinteger(a)
print(result)
