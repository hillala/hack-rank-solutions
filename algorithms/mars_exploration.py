#!/bin/python

import sys


S = raw_input().strip()
error=0
for l in range(len(S)):
    if (l+1)%3==1 and S[l] not in 'S':
        error=error+1
    if (l+1)%3==2 and S[l] not in 'O': 
        error=error+1
    if (l+1)%3==0 and S[l] not in 'S':
        error=error+1
print(error)