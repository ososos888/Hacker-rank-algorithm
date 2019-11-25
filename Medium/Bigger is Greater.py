#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the biggerIsGreater function below.
def biggerIsGreater(arr):
#사전식 순열 알고리즘
#1. a[k] < a[k+1] 인 가장 큰 인덱스 k를 찾는다. 만약 이를 찾을 수 없다면 탐색을 종료한다.
#2. k이후 a[k]보다 큰 값을 가진 가장 먼 인덱스를 찾는다. (a[k] < a[l])
#3. k와 l위치의 값을 교환한다.
#4. 그런다음 k+1 에서 마지막 인덱스 사이를 역순으로 만든다.
    # 이미 Max일 경우
    i = len(arr) - 1
    while i > 0 and arr[i - 1] >= arr[i]:
        i -= 1
    if i <= 0:
        return "no answer"
     
    # 1. 과정
    j = len(arr) - 1
    while arr[j] <= arr[i - 1]:
        j -= 1
    # 3. 과정
    arr[i - 1], arr[j] = arr[j], arr[i - 1]
     
    # 4. 과정
    arr[i : ] = arr[len(arr) - 1 : i - 1 : -1]
    return "".join(arr)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input())

    for T_itr in range(T):
        w = list(input())

        result = biggerIsGreater(w)

        fptr.write(result + '\n')

    fptr.close()
