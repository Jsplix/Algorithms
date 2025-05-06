import sys
input = sys.stdin.readline
# [BOJ] 24079 移動 (Moving) / 수학, 사칙연산
x = int(input())
y = int(input())
z = int(input())

print(1 if x + y < z + 0.5 else 0)