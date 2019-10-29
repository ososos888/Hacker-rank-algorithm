#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):

    h=s[0:2]
    m=s[2:8]
    k=s[8:10]

    if k == 'PM':
        h = int(h) + 12
    return str(h)+m



if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
