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
    return sort
