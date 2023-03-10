import sys
input = sys.stdin.readline
# [BOJ] 2444 별 찍기 - 7 / 구현
n = int(input())
for i in range(n):
    if i == n: print('*'*(2*n-1))
    else:
        for j in range(n - i - 1): print(" ", end='')
        print("*"*(2*i+1))
for i in range(n-1, 0, -1):
    for j in range(n-i): print(" ", end='')
    print("*"*(2*(i-1)+1))