import sys
input = sys.stdin.readline
# [BOJ] 레퓨닛의 덧셈 / 수학, 사칙연산
x, y = map(int, input().split())
print(int('1'*x) + int('1'*y))