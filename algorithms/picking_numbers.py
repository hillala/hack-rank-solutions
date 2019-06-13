#!/bin/python

import sys


n = int(raw_input().strip())
a = map(int,raw_input().strip().split(' '))
a.sort()
v = [a[i+1]-a[i] for i in range(n-1)]

max_pick=0
for x in range(len(v)):
    seq=v[x::]
    if max_pick>len(seq):
        break
    flag=0
    ind=0
    while flag==0:
        if sum(seq[0:ind+1])<2 and ind<len(seq):
            ind=ind+1
        else:
            local_max=ind
            flag=1
    if local_max>max_pick:
        max_pick=local_max

print(max_pick+1)        
