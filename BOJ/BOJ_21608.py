import sys
input = sys.stdin.readline
# [BOJ] 21608 상어 초등학교 / 구현
n = int(input())
seats = [[0 for _ in range(n+1)] for __ in range(n+1)]
lst = [list(map(int, input().split())) for _ in range(n**2)]

dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]
for students in lst:
    now = students[0]
    possible = []

    for r in range(1, n+1):
        for c in range(1, n+1):
            if not seats[r][c]: # 선택되지 않은 seats라면
                like = 0 # 선호도
                empty = 0 # 인접한 자리의 공백 개수

                for k in range(4):
                    nr = r + dr[k]
                    nc = c + dc[k]

                    if 1 <= nr <= n and 1 <= nc <= n:
                        if seats[nr][nc] in students[1:]: like += 1
                        if not seats[nr][nc]: empty += 1
                
                possible.append([like, empty, r, c])
    
    possible.sort(key= lambda x: (-x[0], -x[1], x[2], x[3]))
    seats[possible[0][2]][possible[0][3]] = now

answer = 0
lst.sort() # 1번 학생부터 차례대로 행복도 확인
for i in range(1, n+1):
    for j in range(1, n+1):
        chk = 0
        now = seats[i][j]

        for k in range(4):
            ni = i + dr[k]
            nj = j + dc[k]

            if 1 <= ni <= n and 1 <= nj <= n:
                if seats[ni][nj] in lst[now-1][1:]:
                    chk += 1
        
        answer += 10**(chk-1) if chk else 0

print(answer)