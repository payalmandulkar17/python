#*Lilah has a string, , of lowercase English letters that she repeated infinitely many times.

#Given an integer, , find and print the number of letter a's in the first  letters of Lilah's infinite string.

#For example, if the string is s=aba and n=10 , the substring we consider is abaabaabaa, the first  characters of her infinite string. There are  occurrences of a in the substring. 7
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    #s,n=input.strip(),int(input.strip())
    output=s.count("a")*(n//len(s))+s[:n%len(s)].count("a")
    return output

if __name__ == '__main__':
   

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    print(result)
