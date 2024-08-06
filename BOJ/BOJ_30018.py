import sys
input = sys.stdin.readline
# [BOJ] 30018 타슈 / 수학, 그리디, 사칙연산
n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

count = 0
for i in range(n):
    if A[i] < B[i]:
        count += (B[i] - A[i])

print(count)