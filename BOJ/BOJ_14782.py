import sys
input = sys.stdin.readline
# [BOJ] 14782 Bedtime Reading, I / 수학, 브루트포스, 정수론
n = int(input())
answer = 0
for i in range(1, n+1):
    if n % i == 0:
        answer += i
print(answer)