from math import *
from collections import *
from sys import *
from os import *

## Read input as specified in the question.
## Print output as specified in the question.
n=int(input())

last2=0
last1=1
for i in range(n-1):
    curr=last1+last2
    last2=last1
    last1=curr
print(last1)
