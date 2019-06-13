#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the toys function below.
def toys(w):
    w.sort()
    i=0
    cont=1
    pivot=w[0]
    while i<len(w)-1:
        i=i+1
        if pivot+4<w[i]:
            cont=cont+1
            pivot=w[i]
    return cont

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    w = list(map(int, input().rstrip().split()))

    result = toys(w)

    fptr.write(str(result) + '\n')

    fptr.close()
