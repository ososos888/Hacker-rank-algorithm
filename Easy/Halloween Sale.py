#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the howManyGames function below.
def howManyGames(p, d, m, s):
    # Return the number of games you can buy
    # p 시작값 d 할인값 m 최소값 s 예산
    # p-d needs compare with m
    # if totalprice over than s then end the loof
    # return to # of game
    totalprice = 0
    lcost = 0
    number = 0
    while s >= 0:
        s -= p
        if p-d <= m:
            p = m
        else:
            p -= d
        number += 1
    return number-1
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    pdms = input().split()

    p = int(pdms[0])

    d = int(pdms[1])

    m = int(pdms[2])

    s = int(pdms[3])

    answer = howManyGames(p, d, m, s)

    fptr.write(str(answer) + '\n')

    fptr.close()