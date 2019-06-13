#!/bin/python

import sys


n = int(raw_input().strip())
for j in xrange(n):
    str1=''
    for i in xrange(j+1,n):
        str1=str1+' '
    for i in xrange(n-j-1,n):
        str1=str1+'#'
    print(str1)

