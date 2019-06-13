#!/bin/python

import sys

def getTotalX(a, b):
    # Complete this function
    x2=min(b)
    x1=max(a)
    count=0
    flag=1
    for x in xrange(x1,x2+2):
        if flag==0:
            count=count+1
        flag=0
        for aa in a:
            if x % aa !=0:
                flag=1
                break
        for bb in b:
            if bb %x !=0:
                flag=1
                break
    return count     
        
n, m = raw_input().strip().split(' ')
n, m = [int(n), int(m)]
a = map(int, raw_input().strip().split(' '))
b = map(int, raw_input().strip().split(' '))
total = getTotalX(a, b)
print(total)
