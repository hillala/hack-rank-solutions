#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the quickSort function below.
def quickSort(arr):
    pivot=arr[0]
    left=[]
    right=[]
    for a in arr[1:]:
        if a>pivot:
            right=right+[a]
        if a<pivot:    
            left=left+[a]
    return left+[pivot]+right

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = quickSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
