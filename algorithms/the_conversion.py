#!/bin/python

import sys

def timeConversion(s):
    # Complete this function
    if s[-2:]=='PM':
        h=int(s[:2])+12
        if h==24:
            h='12'
        else:
            h=str(h)
        if len(h)==1:
            h='0'+h
    else:
        h=int(s[:2])
        if h==12:
            h='00'
        else:
            h=str(h)
        
        if len(h)==1:
            h='0'+h
    t=str(h)+s[2:8]
    return t
s = raw_input().strip()
result = timeConversion(s)
print(result)
