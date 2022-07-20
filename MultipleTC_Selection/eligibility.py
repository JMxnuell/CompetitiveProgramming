# Problem: "Eligilibity"
# Judge: kattis
# Resource: https://open.kattis.com/problems/eligibility

from posixpath import split
import sys

n = int(input())
while(n):
    n -= 1
    inp = sys.stdin.readline()
    L = list(map(str,inp.split()))
    secundary = list(map(int,L[1].split("/")))
    birth = list(map(int,L[2].split("/")))
    if(secundary[0] >= 2010 or birth[0] >= 1991):
        print(f"{L[0]} eligible")
    elif(int(L[3]) > 40):
        print(f"{L[0]} ineligible")
    else:
        print(f"{L[0]} coach petitions")
