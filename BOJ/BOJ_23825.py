import sys
input = sys.stdin.readline
# [BOJ] 23825 SASA 모형을 만들어보자 / 수학, 사칙연산
n, m = map(int, input().split())
print(min(n, m) // 2)