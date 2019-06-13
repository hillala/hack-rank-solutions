#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the closestNumbers function below.
def closestNumbers(arr):
    arr.sort()
    dist = [arr[i+1]-arr[i] for i in range(len(arr)-1)]
    val=min(dist)
    min_num=[]

    for d in range(len(dist)):
        if dist[d]==val:
            min_num=min_num+[arr[d]]
            min_num=min_num+[arr[d+1]]
    return min_num

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
