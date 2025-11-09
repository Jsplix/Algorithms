import sys
input = sys.stdin.readline
# [BOJ] 34306 M-Climb Road / 수학, 사칙연산
n = int(input())
w = int(input())
print((n * 5280) // w)