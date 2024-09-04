import sys
import heapq
input = sys.stdin.readline
# [BOJ] 16957 체스판 위의 공 / DP, 자료 구조, 그래프 이론, 그래프 탐색, 분리 집합
dr = [1, 0, -1, -1, -1, 0, 1, 1]
dc = [-1, -1, -1, 0, 1, 1, 1, 0]

def search(pr, pc):
    global r, c

    mn = chess[pr][pc]
    pos = [pr, pc]
    for i in range(8):
        nr = pr + dr[i]
        nc = pc + dc[i]

        if 0 <= nr < r and 0 <= nc < c:
            if chess[nr][nc] < mn:
                mn = chess[nr][nc]
                pos[0] = nr
                pos[1] = nc
    
    return pos

# (sr, sc)에서 (tr, tc)로 공을 옮김
def move(sr, sc, tr, tc):
    balls[tr][tc] += balls[sr][sc]
    balls[sr][sc] = 0

r, c = map(int, input().split())
chess = [list(map(int, input().split())) for _ in range(r)]
balls = [[1 for _ in range(c)] for __ in range(r)]

pq = []
for i in range(r):
    for j in range(c):
        heapq.heappush(pq, [-chess[i][j], i, j])

while pq:
    val, sr, sc = heapq.heappop(pq)
    p = search(sr, sc)
    if [sr, sc] != p:
        move(sr, sc, p[0], p[1])

for row in balls:
    print(*row)