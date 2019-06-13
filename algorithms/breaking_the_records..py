#!/bin/python

import sys

def getRecord(s):
    # Complete this function
    max_val=s[0] 
    min_val=s[0]
    max_count=0
    min_count=0
    for i in xrange(1,len(s)):
        if s[i]>max_val:
            max_val=s[i]
            max_count=max_count+1
        if s[i]<min_val:
            min_val=s[i]
            min_count=min_count+1
            
    return (max_count,min_count)
    
n = int(raw_input().strip())
s = map(int, raw_input().strip().split(' '))
result = getRecord(s)
print " ".join(map(str, result))
