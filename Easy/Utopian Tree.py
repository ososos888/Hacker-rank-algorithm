#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the utopianTree function below.
def utopianTree(n):
    #봄에는 2배성장 여름에는 +1 성장 높이는 1에서 시작
    a = 1
    for i in range(n):
        if i%2 ==0:
            a = a*2
        else:
            a += 1
    return a


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = utopianTree(n)

        fptr.write(str(result) + '\n')

    fptr.close()
