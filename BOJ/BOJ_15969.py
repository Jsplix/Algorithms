import sys
input = sys.stdin.readline
# [BOJ] 15969 행복 / 수학, 구현, 사칙연산
n = int(input())
scores = list(map(int, input().split()))
print(max(scores)-min(scores))