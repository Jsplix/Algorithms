import sys
input = sys.stdin.readline
# [BOJ] 1068 트리 / 그래프 이론, 그래프 탐색, 트리, DFS
n = int(input())
node = list(map(int, input().split()))
r = int(input())
answer = 0

def dfs(idx):
    node[idx] = -2
    for i in range(len(node)):
        if idx == node[i]:
            dfs(i)

dfs(r)
for i in range(n):
    if node[i] != -2 and i not in node:
        answer += 1

print(answer)