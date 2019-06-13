#!/bin/python

import sys

def solve(n, p):
    # Complete this function
    if n%2==0:
        if n-p <n//2:
            return (n-p)//2+(n-p)%2
        else:
           return p//2
    else:
        if n-p <=n//2:
            return (n-p)//2
        else:
            return p//2
    

n = int(raw_input().strip())
p = int(raw_input().strip())
result = solve(n, p)
print(result)
