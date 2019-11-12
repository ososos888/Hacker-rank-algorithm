#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the viralAdvertising function below.
def viralAdvertising(n):
    d = []
    firstday = 2
    today = 0
    nextday = 0
    for i in range(n):
        if i == 0:
            d.append(firstday)
            nextday = firstday*3
        else:
            today = nextday//2
            d.append(today)
            nextday = today*3
    return (sum(d))  

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()