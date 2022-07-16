# Problem: "different"
# Judge: kattis
# Resource: https://open.kattis.com/problems/different
import sys
for line in sys.stdin.readlines():
    l = line.split()
    r = abs(int(l[0])-int(l[1]))
    print(r)