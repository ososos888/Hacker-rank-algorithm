#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    # Write your code here
    b = list(set(a))
    c = 0
    d = []
    if (len(b) == 1):
        c = len(a) 
    else:
        for i in range(len(b)-1):
            d.append(a.count(b[i]))
            if(abs(b[i]-b[i+1]) <= 1):
                d.append(a.count(b[i]) + a.count(b[i+1]))
        c = max(d) 
    return c

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()