import sys
input = sys.stdin.readline
# [BOJ] 31922 이 대회는 이제 제 겁니다 / 수학, 사칙연산
a, b, c = map(int, input().split())
print(max(a+c, b))