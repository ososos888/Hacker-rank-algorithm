#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the squares function below.
def squares(a, b):
    if math.sqrt(a) == int(math.sqrt(a)): #작은수가 거듭제곱수면 +1을 해야 한다
        dif = int(math.sqrt(b)) - int(math.sqrt(a)) + 1
    else:
        dif = int(math.sqrt(b)) - int(math.sqrt(a))    
    return dif


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        ab = input().split()

        a = int(ab[0])

        b = int(ab[1])

        result = squares(a, b)

        fptr.write(str(result) + '\n')

    fptr.close()
