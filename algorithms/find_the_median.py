#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the findMedian function below.
def findMedian(arr):
    arr.sort()
    num=len(arr)//2
    return arr[num]
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = findMedian(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
