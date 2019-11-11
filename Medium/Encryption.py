#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the encryption function below.
def encryption(s):
    #문자열은 공백이 제거된 상태로 입력된다.
    #문자열의 길이를 확인 해 제곱근을 구한다.
    lenofs = len(s)
    lenofs = lenofs**0.5
    #floor, ceil 함수 값을 구한다.
    floors = int(lenofs)
    ceils = floors + 1
    #len(s)가 완전 제곱일 경우 / floor*ceil<len(s)일 경우의 조건식
    if issquare(len(s)) == True:
        floors = int(lenofs)
        ceils = floors
    elif floors * ceils < len(s):
        floors = int(lenofs) + 1
        ceils = floors
    #2차원 배열 생성
    d = [[0 for x in range(ceils)] for y in range(floors)]
    answer = ''
    k=0
    #2차원 배열에 값을 순서대로 할당
    for i in range(floors):
        for j in range(ceils):
            if k < len(s):
                d[i][j]=s[k]
                print(d)
                k += 1
    #2차원 배열을 통해 정답 생성
    for i in range(ceils):
        for j in range(floors):    
            if d[j][i] != 0:
                answer += d[j][i]
        answer += ' '
    
    return answer
#완전제곱을 구하는 함수
def issquare(n):
    return int(n ** 0.5) ** 2 == n


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
