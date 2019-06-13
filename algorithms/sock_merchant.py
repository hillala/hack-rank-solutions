#!/bin/python

import sys

def sockMerchant(n, ar):
    # Complete this function
    l=list(set(ar))
    counter=0
    for i in l:
        counter=counter+(len([j for j in ar if j==i])//2)
    return counter
n = int(raw_input().strip())
ar = map(int, raw_input().strip().split(' '))
result = sockMerchant(n, ar)
print(result)
