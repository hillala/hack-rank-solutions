#!/bin/python

import sys

def super_reduced_string(s):
    # Complete this function
    count=0
    while count<len(s)-1:
        if s[count]==s[count+1]:
            ss=s[:count]+s[count+2:]
            count=0
            s=ss
        else:
            count+=1
    if len(s)==0:
        s='Empty String'
    return s
                
                
s = raw_input().strip()
result = super_reduced_string(s)
print(result)
