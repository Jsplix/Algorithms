import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
# keypoint는 1에서부터의 최대 거리와 최대 거리를 가진 곳부터 다시 최대거리를(총 2번) 구하는 것.
# r1, r2를 -1로 초기화해주는 이유 -> 0으로 해줄 경우 최대 거리를 가진 곳에서
# DFS를 처리하면 본인으로 되돌아오게 됨 (그 때가 당연히 최대가 됨)
# -1로 초기화해주고 시작지점을 0으로하면 검사할 때 -1이 아니므로 본인으로 돌아가지 않음.
def dfs(idx, r):
    for v, d in graph[idx]:
        if r[v] == -1:
            r[v] = r[idx] + d
            dfs(v, r)

n = int(input())
graph = [[] for _ in range(n + 1)]
dist = {}
r1 = [-1 for _ in range(n + 1)]
r1[1] = 0
for _ in range(n):
    tmp = list(map(int, input().split()))
    i = 1
    while i != len(tmp) - 1:
        graph[tmp[0]].append([tmp[i], tmp[i + 1]])
        i += 2

dfs(1, r1)
tmp = 0
tmp_idx = 0

for i in range(1, len(r1)):
    if r1[i] > tmp:
        tmp = r1[i]
        tmp_idx = i
r2 = [-1 for _ in range(n + 1)]
r2[tmp_idx] = 0
dfs(tmp_idx, r2)
print(max(r2))