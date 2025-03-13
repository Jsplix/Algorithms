import sys
input = sys.stdin.readline
# [BOJ] 2522 별 찍기 - 12 / 구현
n = int(input())
for i in range(n-1):
    print(" "*(n-i-1) + "*"*(i+1))
print("*"*n)
for j in range(n-1):
    print(" "*(j+1)+"*"*(n-j-1))