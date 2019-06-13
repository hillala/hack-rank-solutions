#!/bin/python

import sys


n = int(raw_input().strip())
a = map(int, raw_input().strip().split(' '))
# your code goes here
#aa=[abs(i) for i in a]
a.sort()
print(min([abs(a[i+1]-a[i]) for i in range(n-1)]))
#print (min([min([abs(aa[i]-aa[x]) for x in range(i+1,n)]) for i in range(n-1)]))
