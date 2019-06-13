#!/bin/python

import math
import os
import random
import re
import sys

numbers = "0123456789"
lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
special_characters = "!@#$%^&*()-+"

# Complete the minimumNumber function below.
def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    letters=set([p for p in password])
    any_in = lambda a, b: bool(set(a).intersection(b))
    add=0
    if not any_in(letters,numbers):
        add=add+1
    if not any_in(letters,lower_case):
        add=add+1
    if not any_in(letters,upper_case):
        add=add+1
    if not any_in(letters,special_characters):
        add=add+1
    if len(password)+add>5:
        return add
    else:
        add_d=6-(add+len(password))    
        return add_d+add


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    password = raw_input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
