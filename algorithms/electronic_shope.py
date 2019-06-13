#!/bin/python

import sys

def getMoneySpent(keyboards, drives, s):
    # Complete this function
    buy=-1
    for k in keyboards:
        for d in drives:
            v_sum=k+d
            if buy<v_sum and v_sum<=s:
                buy=v_sum
    return (buy)
s,n,m = raw_input().strip().split(' ')
s,n,m = [int(s),int(n),int(m)]
keyboards = map(int, raw_input().strip().split(' '))
drives = map(int, raw_input().strip().split(' '))
#  The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
moneySpent = getMoneySpent(keyboards, drives, s)
print(moneySpent)
