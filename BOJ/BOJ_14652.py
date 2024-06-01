import sys
input = sys.stdin.readline
# [BOJ] 14652 나는 행복합니다~ / 수학, 사칙연산
n, m, k = map(int, input().split())
print(k // m, k % m)