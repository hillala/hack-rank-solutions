#!/bin/python

import sys


t = int(raw_input().strip())
for a0 in xrange(t):
    b,w = raw_input().strip().split(' ')
    b,w = [long(b),long(w)]
    x,y,z = raw_input().strip().split(' ')
    x,y,z = [long(x),long(y),long(z)]
    price=0
    if min(x,y)+z>=max(x,y):
        price=b*x+y*w
    else:
        if x<y:
            price=x*(b+w)+w*z
        else:
            price=y*(b+w)+b*z
    print(price)
                