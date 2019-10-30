#!/bin/python3

import os
import sys

#
# Complete the pageCount function below.
#
def pageCount(n, p):

    #n은 마지막 페이지, p는 가고자 하는 페이지
    #p/2의 몫은 첫페이지로부터 넘기는 횟수
    #n/2의 몫은 첫페이지부터 마지막페이지까지 가는 횟수
    #따라서 n//2-p//2는 마지막 페이지부터 원하는 페이지로 가는 횟수
    a = min(p//2,n//2-p//2)
    return (a)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = int(input())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()