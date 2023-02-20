import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
# [BOJ] 2263 트리의 순회 / 트리, 재귀, 분할 정복
n = int(input())
in_order = [-1] + list(map(int, input().split()))
post_order = [-1] + list(map(int, input().split()))

pos = [-1 for _ in range(n+1)]
for i in range(n+1):
    pos[in_order[i]] = i # pos는 in_order[i]에서 i의 index를 저장

answer = []
def solve(in_start, in_end, post_start, post_end):
    if (in_start > in_end) or (post_start > post_end): return
    
    root = post_order[post_end] # 후위 순회의 마지막 노드는 최상위 노드(루트 노드)임
    size = pos[root] - in_start
    answer.append(root)

    solve(in_start, pos[root]-1, post_start, post_start + size - 1)
    solve(pos[root]+1, in_end, post_start + size, post_end - 1)
solve(1, n, 1, n)
print(*answer)