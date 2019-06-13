#!/bin/python

import sys


s = raw_input().strip()
n = long(raw_input().strip())
b=0
if len(s)>n:
    num=len([i for i in range(n) if s[i]=='a'])
    print(num)
else:
    var1=n // len(s)
    var2= n %len(s)
    b=len([i for i in s if i == 'a'])*var1
    if var2>0:         
        print(len([i for i in range(var2) if s[i]=='a'])+b)
    else:
        print(b)

