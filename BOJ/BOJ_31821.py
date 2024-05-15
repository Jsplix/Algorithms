import sys
input = sys.stdin.readline
# [BOJ] 31821 학식 사주기 / 구현
n = int(input())
prices = [int(input()) for _ in range(n)]
m = int(input())

answer = 0
for i in range(m):
    b = int(input())
    answer += prices[b-1]
print(answer)