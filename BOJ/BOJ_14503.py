import sys
input = sys.stdin.readline
# [BOJ] 14503 로봇 청소기 / 구현, 시뮬레이션
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

n, m = map(int, input().split())
r, c, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]

visited[r][c] = 1
cnt = 1

while True:
    flag = False # 청소 확인 용도. False - 청소 안함, True - 청소함.
    for i in range(4):
        d = (d+3) % 4
        nr = r + dr[d]
        nc = c + dc[d]

        if 0 <= nc < m and 0 <= nr < n and room[nr][nc] == 0:
            if not visited[nr][nc]:
                visited[nr][nc] = 1
                cnt += 1
                c, r = nc, nr
                flag = True # 청소 처리
                break 

    if not flag: # 청소하지 않은 경우
        if room[r-dr[d]][c-dc[d]] == 1:
            print(cnt)
            break
        else:
            r = r - dr[d]
            c = c - dc[d]
