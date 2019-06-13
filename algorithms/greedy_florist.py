#!/bin/python

import sys

def getMinimumCost(n, k, c):
    # Complete this function
    c.sort(reverse=True)
    if n<=k:
        sum_pay=sum(c)
    else:
        sum_pay=sum(c[0:k])
        c=c[k:]
        counter=2
        while len(c)>k:
            sum_pay=sum_pay+sum(c[0:k])*counter
            c=c[k:]
            counter=counter+1
        if len(c)>0:
            sum_pay=sum_pay+sum(c)*counter
    return sum_pay
n, k = raw_input().strip().split(' ')
n, k = [int(n), int(k)]
c = map(int, raw_input().strip().split(' '))
minimumCost = getMinimumCost(n, k, c)
print(minimumCost)
