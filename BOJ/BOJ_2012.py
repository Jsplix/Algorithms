import sys
input = sys.stdin.readline
# [BOJ] 2012 등수 매기기 / 그리디, 정렬
n = int(input())
ranks = sorted(int(input()) for _ in range(n))

answer = 0
for i in range(1, n+1):
    answer += abs(i - ranks[i-1])
print(answer)