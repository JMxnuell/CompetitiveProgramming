# Problem: "Time Travelling Temperatures"
# Judge: kattis
# Resource: https://open.kattis.com/problems/temperature

from posixpath import split
import sys


inp = sys.stdin.readline()
L = list(map(int,inp.split()))

if((not L[0]) and L[1] == 1):
    print("ALL GOOD")
elif(L[1] == 1):
    if((not L[0])):
        print("0")
    else:
        print("IMPOSSIBLE")
else:
    print(str(L[0]/(1-L[1])))

    