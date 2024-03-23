import sys
input = sys.stdin.readline
# [BOJ] 2458 키 순서 / 그래프 이론, 그래프 탐색, DFS, 최단 경로, 플로이드 워셜
n, m = map(int, input().split())
height = [[0 for _ in range(n+1)] for __ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    height[b][a] = 1

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if height[i][k] and height[k][j]: # i가 k번보다 키가 크고, k번은 j번보다 크다.
                height[i][j] = 1 # 그런 경우, i가 j번보다도 키가 크다.

answer = 0
for i in range(1, n+1): # 기준이 되는 학생
    cnt = 0
    for j in range(1, n+1):
        cnt += (height[i][j] + height[j][i]) # 기준보다 작은 키의 학생 수 + 기준보다 큰 키의 학생 수
    if cnt == n-1: # 총 합이 n-1인 경우 → 자기 자신의 순서를 알 수 있음.
        answer += 1
print(answer)