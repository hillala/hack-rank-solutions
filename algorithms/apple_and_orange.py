#!/bin/python

import sys


s,t = raw_input().strip().split(' ')
s,t = [int(s),int(t)]
a,b = raw_input().strip().split(' ')
a,b = [int(a),int(b)]
m,n = raw_input().strip().split(' ')
m,n = [int(m),int(n)]
apple = map(int,raw_input().strip().split(' '))
orange = map(int,raw_input().strip().split(' '))

v_apple=0
for x in apple:
    if x+a>s-1 and x+a<t+1:
        v_apple=v_apple+1
        
v_orange=0
for x in orange:
    if x+b>s-1 and x+b<t+1:
        v_orange=v_orange+1

print(v_apple)
print(v_orange)