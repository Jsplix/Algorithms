import sys
input = sys.stdin.readline
# [BOJ] 14267 회사 문화 1 / DP, 그래프 이론, 그래프 탐색, 트리, DFS, 트리 DP
n, m = map(int, input().split())
boss = [0] + list(map(int, input().split()))

praise = [0 for _ in range(n+1)]

for _ in range(m):
    who, p = map(int, input().split())
    praise[who] += p

for i in range(2, n+1):
    praise[i] += praise[boss[i]]

print(*praise[1:])