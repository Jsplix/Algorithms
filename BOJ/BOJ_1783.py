import sys
input = sys.stdin.readline
# [BOJ] 1783 병든 나이트 / 구현, 그리디, 많은 조건 분기
n, m = map(int, input().split())

if n == 1:
    print(1)
elif n == 2:
    print(min(4, (m+1)//2))
elif m <= 6:
    print(min(4, m))
else:
    print(m-2)