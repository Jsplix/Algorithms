import sys
input = sys.stdin.readline
# [BOJ] 12760 최후의 승자는 누구? / 구현, 정렬, 시뮬레이션
n, m = map(int, input().split())
cards = [sorted(map(int, input().split())) for _ in range(n)]

mx = [max(col) for col in zip(*cards)]
scores = [0 for _ in range(n)]

for seq in range(m):
    chk = mx[seq]
    for i in range(n):
        if cards[i][seq] == chk:
            scores[i] +=1

mx_score = max(scores)
result = []
for i in range(n):
    if scores[i] == mx_score:
        result.append(i+1)

print(*result)