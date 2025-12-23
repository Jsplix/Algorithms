import sys
input = sys.stdin.readline
# [BOJ] 29767 점수를 최대로 / 그리디, 정렬, 누적 합
n, k = map(int, input().split())
A = list(map(int, input().split()))
asum = [[0, i] for i in range(n)]

asum[0][0] = A[0]
for i in range(1, n):
    asum[i][0] = A[i] + asum[i - 1][0]

asum.sort(key= lambda x:(-x[0]))

answer = 0
for i in range(k):
    answer += asum[i][0]
print(answer)