#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the findDigits function below.
def findDigits(n):
    d = []
    #문자열로 분해하고 다시 int로 전환 후 0이 아니면 나누어서 확인
    d = list(str(n))
    d = list(map(int, d))
    countn = 0
    for i in range(0, len(d)):
        if d[i] != 0:
            if n%d[i] == 0:
                countn += 1
    return countn
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = findDigits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
