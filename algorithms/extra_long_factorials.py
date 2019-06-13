#!/bin/python

import sys


n = int(raw_input().strip())
s=n
for i in range(n-1):
    s=s*(i+1)
print(s)