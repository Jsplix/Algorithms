import sys
input = sys.stdin.readline
# [BOJ] 10419 지각 / 수학, 구현, 브루트포스, 사칙연산
for _ in range(int(input())):
    n = int(input())
    if n == 1: print(0)
    
    for i in range(int(n ** 0.5) + 1, 0, -1):
        if i ** 2 + i <= n: 
            print(i)
            break