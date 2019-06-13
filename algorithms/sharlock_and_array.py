#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the balancedSums function below.
def balancedSums(arr):
    if len(arr)==1:
        return 'YES'
    else:
        right=sum(arr[1:])
        left=0
        val='NO'
        for k in range(len(arr)-1):
            if left==right:
                val='YES'
                break
            else:
                right=right-arr[k+1]
                left=left+arr[k]
    return val

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = balancedSums(arr)

        fptr.write(result + '\n')

    fptr.close()
