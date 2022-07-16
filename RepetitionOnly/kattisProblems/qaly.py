# Problem: "Quality-Adjusted Life-Year"
# Judge: kattis
# Resource: https://open.kattis.com/problems/qaly

from operator import mul
import functools
import sys

inputs = iter(sys.stdin.readlines())
TC = int(next(inputs))
r = 0.0
for _ in range(TC):
    r += functools.reduce(mul, map(float, next(inputs).split()))

print(r)