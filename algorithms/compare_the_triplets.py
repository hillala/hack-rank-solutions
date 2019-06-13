#!/bin/python

import sys

def solve(a0, a1, a2, b0, b1, b2):
    # Complete this function
    a=0
    b=0
    a,b=function1(a0,b0,a,b)
    a,b=function1(a1,b1,a,b)
    a,b=function1(a2,b2,a,b)
    return a,b

def function1 (num1,num2,p1,p2):
    if num1>num2:
        p1+=1
    elif num2>num1:
        p2+=1
    return p1,p2
a0, a1, a2 = raw_input().strip().split(' ')
a0, a1, a2 = [int(a0), int(a1), int(a2)]
b0, b1, b2 = raw_input().strip().split(' ')
b0, b1, b2 = [int(b0), int(b1), int(b2)]
result = solve(a0, a1, a2, b0, b1, b2)
print " ".join(map(str, result))


