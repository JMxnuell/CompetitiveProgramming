# Problem: "Moscow Dream"
# Judge: kattis
# Resource: https://open.kattis.com/problems/moscowdream

from posixpath import split
import sys


inp = sys.stdin.readline()
L = list(map(int,inp.split()))

if(L[3] >= 3 and L[0] and L[1] and L[2]):
    if(L[0]+L[1]+L[2] >= L[3]):
        print("YES")
    else:
        print("No")
else:
    print("NO")
    