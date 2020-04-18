import math
import os
import random
import re
import sys
def cloud(c):
    i=0
    jump=-1
    n=len(c)
    while i<n:
        if i<n-2 and c[i+2]==0:i+=1
        jump+=1
        i+=1    
        """ if(c[i+1]==0):
            jump=jump+1
            i=i+1
        elif(c[i+2]==0):
            jump=jump+1
            i=i+2 """
    return jump


if __name__=='__main__': 
    n=input()
    c=list(map(int,input().rstrip().split())) 
    result=cloud(c)
    print(result)
