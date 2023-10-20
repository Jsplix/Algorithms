import sys
input = sys.stdin.readline
# [BOJ] 5724 파인만 / 수학, 사칙연산
while True:
    n = int(input())
    if n == 0: break
    print((n*(n+1)*(2*n+1))//6)