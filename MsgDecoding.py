import math
import os
import random
import re
import sys

def decode(s):
    for i in range(len(s)-1):
        x=s[i][i]*10+s[i][i+1]          
      
    return x
if __name__=='__main__':
    n=int(input())
    for i in range(n):
         length=int(input())
         c=list(map(int,input().rstrip().split())) 
         result=decode(c)
         print(result)
        
     
         
