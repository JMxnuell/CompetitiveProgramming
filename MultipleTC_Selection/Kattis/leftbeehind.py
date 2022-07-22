# Problem: "Left Beehind"
# Judge: kattis
# Resource: https://open.kattis.com/problems/leftbeehind

import sys

for line in sys.stdin.readlines():
    if line == '0 0\n':
        break
    t = tuple(map(int,line.split()))
    if t[0]+t[1] == 13:
        print("Never speak again.")
    elif t[1] > t[0]:
        print("Left beehind.")
    elif t[0] > t[1]:
        print("To the convention.")
    else:
        print("Undecided.")