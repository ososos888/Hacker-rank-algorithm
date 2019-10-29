#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the appendAndDelete function below.
def appendAndDelete(s, t, k):
    slen = len(s)
    tlen = len(t)
    i = 0
    a = 0
    b = 0
    if slen == tlen:
        return 'Yes'
    else:
        if slen>tlen:
            b = slen-tlen
            while i == tlen:
                if s[i] != t[i]:
                    a = a+2
                    i = i+1
                else:
                    a = a
        elif slen<tlen:
            b = slen-tlen
            while i == slen:
                if s[i] != t[i]:
                    a = a+2
                    i = i+1
                else:
                    a = a
        a = a + b    
        if a<k:
            return 'Yes'
        else:
            return 'No'






if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()
