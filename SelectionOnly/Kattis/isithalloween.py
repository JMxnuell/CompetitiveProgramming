# Problem: "IsItHalloween.com"
# Judge: kattis
# Resource: https://open.kattis.com/problems/isithalloween


from posixpath import split
import sys


inp = sys.stdin.readline()
L = inp.split()
if  L[0] == "OCT" and L[1] == "31":
    print("yup")
else:
    print("nope")