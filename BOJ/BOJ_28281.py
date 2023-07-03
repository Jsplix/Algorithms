import sys
input = sys.stdin.readline
# [BOJ] 28281 선물 / 수학, 구현, 사칙연산
n, x = map(int, input().split())
arr = list(map(int, input().split()))
answer = [0 for _ in range(n-1)]

for i in range(n-1):
    answer[i] = arr[i] + arr[i+1]

print(min(answer)*x)