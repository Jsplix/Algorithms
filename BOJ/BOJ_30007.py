import sys
input = sys.stdin.readline
# [BOJ] 30007 라면 공식 / 수학, 구현, 사칙연산
for _ in range(int(input())):
    a, b, x = map(int, input().split())
    print(a*(x-1)+b)