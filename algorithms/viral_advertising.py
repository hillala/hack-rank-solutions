#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the viralAdvertising function below.
def viralAdvertising(n):
    likes_sum=2
    likes=2
    people=5
    for i in range(n-1):
        people=likes*3
        likes=people//2
        likes_sum=likes_sum+likes
    return likes_sum



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()
