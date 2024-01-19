import sys
input = sys.stdin.readline

# [BOJ] 18808 스티커 붙이기 / 구현, 브루트 포스, 시뮬레이션

def rotation(sticker): # 열은 행이 되고 행은 열이 됨.
    result = [] # 시계 방향 90도 회전
    for i in range(len(sticker[0])):
        col = []
        for j in range(len(sticker)-1, -1, -1):
            col.append(sticker[j][i])
        result.append(col)
    return result

def checking(result, sticker):
    for sy in range(len(sticker)):
        for sx in range(len(sticker[0])):
            if result[y + sy][x + sx] + sticker[sy][sx] > 1:
                return False
    return True

def attaching(result, sticker):
    for sy in range(len(sticker)):
        for sx in range(len(sticker[0])):
            result[y + sy][x + sx] += sticker[sy][sx]
    return

# 규칙 1. 가능한 가장 위, 가장 왼쪽의 위치에 붙임.
# 규칙 2. 스티커를 붙일 수 없다면 회전시킨다.
# 규칙 2-1. 회전을 모두 시켜도 붙일 수 없다면 버린다.

n, m, k = map(int, input().split())
board = [[0 for _ in range(m)] for _ in range(n)]
for i in range(k):
    r, c = map(int, input().split())
    st = [list(map(int, input().split())) for _ in range(r)]

    flag = False
    cnt = 0
    while cnt < 4:
        if flag: break
        for y in range(n - len(st) + 1):
            if flag: break
            for x in range(m - len(st[0]) + 1):
                if checking(board, st):
                    attaching(board, st)
                    flag = True # 붙임
                    break
        if not flag:
            st = rotation(st)
            cnt += 1

answer = 0
for i in range(n):
    for j in range(m):
        answer += board[i][j]
print(answer)