#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    i = 0
    plusct = 0
    minusct = 0
    zeroct = 0

    for i in range(n):
        if arr[i] > 0:
            plusct += 1
        elif arr[i] < 0:
            minusct += 1
        else:
            zeroct += 1    
    pn = plusct/n
    mn = minusct/n
    zn = zeroct/n

    return print('%.6f\n' %pn,'%.6f\n' %mn, '%.6f\n' %zn)

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
