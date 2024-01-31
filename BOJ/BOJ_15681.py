import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
# [BOJ] 15681 트리와 쿼리 / DP, 그래프 이론, 그래프 탐색, 트리, DFS, 트리 DP
n, r, q = map(int, input().split())
trees = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    trees[a].append(b)
    trees[b].append(a)

sizes = [0 for _ in range(n+1)]
def solve(x): # 노드 x의 서브트리 정점 개수 count
    sizes[x] = 1
    for node in trees[x]:
        if not sizes[node]:
            solve(node)
            sizes[x] += sizes[node]

solve(r)

for _ in range(q):
    print(sizes[int(input())])