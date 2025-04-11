import sys
input = sys.stdin.readline
# [BOJ] 25784 Easy-to-Solve Expressions / 수학, 구현, 사칙연산
arr = sorted(map(int, input().split()))
if arr[0] + arr[1] == arr[2]: print(1)
elif arr[0] * arr[1] == arr[2]: print(2)
else: print(3)