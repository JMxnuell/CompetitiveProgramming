# Problem: "Tarifa"
# Judge: kattis
# Resource: https://open.kattis.com/problems/tarifa

X = int(input())
N = int(input())
R = int()

while(N > 0):
    N -= 1
    R += X - int(input())

R += X
print(str(R))
