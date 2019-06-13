#!/bin/python

import sys

def maximumToys(prices, k):
    # Complete this function
    prices.sort()
    sum_pay=0
    number=0
    for p in prices:
        if sum_pay+p<=k:
            sum_pay=sum_pay+p
            number=number+1
        else:
            break
    return number
                
if __name__ == "__main__":
    n, k = raw_input().strip().split(' ')
    n, k = [int(n), int(k)]
    prices = map(int, raw_input().strip().split(' '))
    result = maximumToys(prices, k)
    print result

