#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the larrysArray function below.
def larrysArray(A):
    #숫자가 이동하는 횟수의 총 합이 홀수인 경우에는 정렬할 수 없다(15퍼즐 참조)]
    print (A)
    j = 1
    count = 0
    for i in range(len(A)-1):
        while j < len(A):
            if A[i] > A[j]:
                count += 1
            j += 1
        j = i+1
    if count%2 == 0:
        return ("YES")
    else:
        return ("NO")

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        A = list(map(int, input().rstrip().split()))

        result = larrysArray(A)

        fptr.write(result + '\n')

    fptr.close()
