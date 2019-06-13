#!/bin/python

import math
import os
import random
import re
import sys

# Complete the chocolateFeast function below.
def chocolateFeast(n, c, m):
    choclate=0
    if n//c>0:
        choclate=choclate+n//c
        warps=n//c
        while warps>=m:
            choclate=choclate+warps//m
            warps=warps//m+warps%m
    return  choclate

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(raw_input())

    for t_itr in xrange(t):
        ncm = raw_input().split()

        n = int(ncm[0])

        c = int(ncm[1])

        m = int(ncm[2])

        result = chocolateFeast(n, c, m)

        fptr.write(str(result) + '\n')

    fptr.close()
