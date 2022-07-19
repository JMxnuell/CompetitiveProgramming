# Problem: "Judging Moose"
# Judge: kattis
# Resource: https://open.kattis.com/problems/judgingmoose


import functools
from posixpath import split
import sys


inp = sys.stdin.readline()
L = list(map(int,inp.split()))
if L[0] == L[1]:
    if L[0]:
        print(f"Even {str(L[0]*2)}")
    else:
        print("Not a moose")
else:
    if L[0]>L[1]: print(f"Odd {str(L[0]*2)}")
    else: print(f"Odd {str(L[1]*2)}")