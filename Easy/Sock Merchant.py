#!/bin/python3

import math
import os
import random
import re
import sys
import copy

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    sockslist = copy.deepcopy(ar) #List copy
    sockslist = list(set(sockslist)) #Delete duplication
    a = 0

    for i in range(len(sockslist)):
        a += ar.count(sockslist[i])//2
    return a

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()