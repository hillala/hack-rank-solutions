#!/bin/python

import sys


t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    if n>2:
        c1=n//3
        c2=n//5
        counter=c1
        flag=0
        while counter>=0 and flag==0:
            for j in xrange(c2+1,0,-1):
                if counter*3+(j-1)*5==n:
                    flag=1
                    break
            counter=counter-1
        number=str()
        if flag==1:
            for k in range((counter+1)*3):
                number=number+'5'
            for k in range((j-1)*5):
                number=number+'3'
        else:
            number='-1'
        print(number)
    else:
        print('-1')
                