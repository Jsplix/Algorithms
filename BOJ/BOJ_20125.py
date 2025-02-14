import sys
input = sys.stdin.readline
# [BOJ] 20125 쿠키의 신체 측정 / 구현
n = int(input())
board = [list(input().rstrip()) for _ in range(n)]
visited = [[0 for _ in range(n)] for __ in range(n)]

flag = False
head, heart = [-1, -1], [-1, -1]
back = 0
left_arm, right_arm = 0, 0
left_leg, right_leg = 0, 0
for r in range(n):
    for c in range(n):
        if board[r][c] == '*':
            head = [r, c]
            heart = [r+1, c]
            visited[r][c] = 1
            visited[r+1][c] = 1

            for la in range(c):
                if board[r+1][la] == '*':
                    left_arm += 1
            
            for ra in range(c+1, n):
                if board[r+1][ra] == '*':
                    right_arm += 1

            for i in range(r+2, n):
                if board[i][c] == '*':
                    visited[i][c] = 1
                    back += 1
            
            flag = True
            break

    if flag: break

for i in range(heart[0]+back+1, n):
    if board[i][heart[1]-1] == '*': left_leg += 1
    if board[i][heart[1]+1] == '*': right_leg += 1

print(heart[0]+1, heart[1]+1)
print(left_arm, right_arm, back, left_leg, right_leg)