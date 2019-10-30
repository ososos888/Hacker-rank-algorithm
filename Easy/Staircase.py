#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    d=[]
    for i in range(n):
        #1항 i=0 n=5 공백=5개 #1개
        #2항 i=1 n=5 공백=4개 #2개
        #6항 i=5 n=5 공백=0개 #6개
        #공백 갯수 = n-i #갯수 i+1
        d[:i]=" "*(n-i)
        d[n-i-1:]="#"*(i+1)
        print("".join(d))

if __name__ == '__main__':
    n = int(input())

    staircase(n)

