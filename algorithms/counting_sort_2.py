#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingSort function below.
def countingSort(arr):
    sort = [0] * 100
    for a in arr:
        sort[a]= sort[a]+1
    
    sort_list=[[n] * (sort[n]) for n in range(100) if sort[n]>0]
    chained = []
    
    for i in range(len(sort_list)):
        chained.extend(sort_list.pop(0))
    return chained
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
