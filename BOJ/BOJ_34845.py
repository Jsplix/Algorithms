import sys
input = sys.stdin.readline
# [BOJ] 34845 강의평 / 수학, 브루트포스, 사칙연산
N, X = map(int, input().split())
scores = list(map(int, input().split()))

sm = sum(scores)
avg = sm / N
result = 0
while avg < X:
    sm += 100
    result += 1
    avg = sm / (N + result)

print(result)