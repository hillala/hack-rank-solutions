#!/bin/python

import sys


n = int(raw_input().strip())
A = map(int,raw_input().strip().split(' '))
ans=-1
for l in range(n-1):
    for k in xrange(l+1,n):
        if A[l]==A[k] and (k-l<ans or ans==-1):
            ans=k-l
print(ans)
            