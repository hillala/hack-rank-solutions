#!/bin/python

import sys
def diagonaldiff(a,n):
    x1=0
    x2=0
    for i in range(n):
        x1=x1+a[i][i]
        x2=x2+a[i][n-1-i]
    return abs(x1-x2)        


n = int(raw_input().strip())
a = []
for a_i in xrange(n):
    a_temp = map(int,raw_input().strip().split(' '))
    a.append(a_temp)
print (diagonaldiff(a,n))
    
