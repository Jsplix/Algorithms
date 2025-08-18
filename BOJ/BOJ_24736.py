import sys
input = sys.stdin.readline
# [BOJ] 24736 Football Scoring / 수학, 사칙연산
a = list(map(int, input().split()))
b = list(map(int, input().split()))

A = 6 * a[0] + 3 * a[1] + 2 * a[2] + 1 * a[3] + 2 * a[4]
B = 6 * b[0] + 3 * b[1] + 2 * b[2] + 1 * b[3] + 2 * b[4]
print(A, B)