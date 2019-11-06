#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the divisibleSumPairs function below.
def divisibleSumPairs(n, k, ar):
    #n은 배열의 길이 k는 배수 ar은 배열
    a = 0
    for i in range(n):
        j = i+1
        while j < n:
            if ((ar[i]+ar[j])%k) == 0:
                a += 1
            j += 1
    return a    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    fptr.write(str(result) + '\n')

    fptr.close()