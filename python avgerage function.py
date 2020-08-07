#!/bin/python3

import math
import os
import random
import re
import sys


# write your code here
def avg(*a):
     sum1=0
     avg=0
     for i in range(len(a)):
         sum1=sum1+a[i]
     avg=sum1/len(a)
     return avg
    
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
    nums = list(map(int, input().split()))
    res = avg(*nums)
    
    fptr.write('%.2f' % res + '\n')

    fptr.close()