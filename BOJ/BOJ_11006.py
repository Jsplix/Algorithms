import sys
input = sys.stdin.readline
# [BOJ] 11006 남욱이의 닭장 / 수학, 사칙연산
for _ in range(int(input())):
    n, m = map(int, input().split())
    print(2*m-n, n-m)