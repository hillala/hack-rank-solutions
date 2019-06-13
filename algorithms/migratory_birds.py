#!/bin/python

import sys

def migratoryBirds(n, ar):
    # Complete this function
    birds=list(set(ar))
    birds.sort()
    count=0
    bird=0
    for b in birds:
        sum_bird=len([a for a in ar if a==b])
        if sum_bird>count:
            count=sum_bird
            bird=b
    return bird
             
        
n = int(raw_input().strip())
ar = map(int, raw_input().strip().split(' '))
result = migratoryBirds(n, ar)
print(result)
