from collections import deque
import sys
input = sys.stdin.readline
# [BOJ] 16928 뱀과 사다리 게임 / 그래프 이론, 그래프 탐색, BFS
n, m = map(int, input().split())
move = {}
for _ in range(n+m):
    k, v = map(int, input().split())
    move[k] = v
visited = [0 for _ in range(101)]

def bfs():
    queue = deque([1])
    visited[1] = 1
    
    while queue:
        now = queue.popleft()
        for dice in [1, 2, 3, 4, 5, 6]:
            moved = now + dice
            if 1 <= moved <= 100 and not visited[moved]:
                if moved in move.keys():
                    moved = move[moved]
                if not visited[moved]:
                    queue.append(moved)
                    visited[moved] = visited[now] + 1

bfs()
print(visited[100]-1)