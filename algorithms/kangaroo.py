#!/bin/python

import sys

def kangaroo(x1, v1, x2, v2):
    # Complete this function
    if v1==v2 and x1==x2:
        return 'YES'
    else: 
        if v1==v2 and x1!=x2:
            return 'NO'
        else:
            n=(x1-x2)/float(v2-v1)
            if n>0 and (n %1 )==0:
                return 'YES'
            else:
                return 'NO'

    
 
                
x1, v1, x2, v2 = raw_input().strip().split(' ')
x1, v1, x2, v2 = [int(x1), int(v1), int(x2), int(v2)]
result = kangaroo(x1, v1, x2, v2)
print(result)
