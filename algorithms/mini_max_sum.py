#!/bin/python

import sys

arr = map(int, raw_input().strip().split(' '))
a=sum(arr)
print a-max(arr),a-min(arr)