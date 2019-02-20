#John works at a clothing store. He has a large pile of socks that he must pair by color for sale. Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.

#For example, there are n=7 ar=[1,2,1,2,1,3,2] socks with colors . There is one pair of color  and one of color . There are three odd socks left, one of each color. The number of pairs is 2.
import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    s=set()
    pair=0
    for i in range(n):
        if ar[i] not in s:
            s.add(ar[i])
        else:
            pair=pair+1
            s.remove(ar[i])
    return pair        
                

if __name__ == '__main__':
   

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    print(result)