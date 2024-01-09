import sys
input = sys.stdin.readline
# [BOJ] 8972 미친 아두이노 / 구현, 시뮬레이션
r, c = map(int, input().split())
board = [list(input().rstrip()) for _ in range(r)]
move = list(map(int, input().rstrip()))

jongsu_pos = [(x, y) for x in range(c) for y in range(r) if board[y][x] == 'I'][0]
crazy_pos = [(x, y) for x in range(c) for y in range(r) if board[y][x] == 'R']

dx = [-1, 0, 1, -1, 0, 1, -1, 0, 1]
dy = [1, 1, 1, 0, 0, 0, -1, -1, -1]

def move_jongsu_arduino(direction):
    global jongsu_pos
    # 움직이지 않는 경우 (문제에서는 방향이 1번부터 9번까지, 코드에서는 0부터 시작이므로 -1 해줌)
    if direction == 4: return True 

    tx, ty = jongsu_pos[0] + dx[direction], jongsu_pos[1] + dy[direction] # target_x, target_y - 아두이노의 새로운 위치
    if board[ty][tx] == 'R': # 미친 아두이노 있는 경우
        return False
    else:
        board[jongsu_pos[1]][jongsu_pos[0]] = '.' # 원래 자리는 빈칸으로 바꾸고
        jongsu_pos = (tx, ty) # 종수의 아두이노 위치 업데이트
        board[ty][tx] = 'I' # 업데이트 된 위치에 종수의 아두이노 표시
        return True
    
def move_crazy_arduino():
    global r, c, jongsu_pos, crazy_pos
    pos_after_move = {} # 미친 아두이노 이동 후 해당 위치에 아두이노가 겹치는지 확인
    chk_crazy_arduino_pos = []

    for x, y in crazy_pos:
        board[y][x] = '.' # 기존의 로봇 위치는 '.'으로 바꿔줌
        mn_dist = 201 # r, c 는 각각 100, 100 이므로 종수 아두이노와 미친 아두이노 사의의 거리 최댓값은 200임. +1 해줌.
        mn_pos = (0, 0)
        for i in range(9): 
            if i == 4: continue
            nx = x + dx[i]
            ny = y + dy[i]
            new_dist = abs(nx-jongsu_pos[0]) + abs(ny-jongsu_pos[1]) # 거리를 구함
            if 0 <= nx < c and 0 <= ny < r: # 범위 내에서 확인
                if new_dist < mn_dist: # 최소 거리보다 작으면 갱신 후 해당 위치 저장
                    mn_dist = new_dist
                    mn_pos = (nx, ny)

        if mn_pos == jongsu_pos: # 종수의 아두이노와 만나는 경우
            return False
        chk_crazy_arduino_pos.append(mn_pos)
        if mn_pos in pos_after_move.keys():
            pos_after_move[mn_pos] += 1
        else:
            pos_after_move[mn_pos] = 1
    
    temp = []
    for pos in chk_crazy_arduino_pos:
        if pos in temp or pos_after_move[pos] > 1:
            continue
        temp.append(pos)

    crazy_pos = temp
    for x, y in crazy_pos:
        board[y][x] = 'R' # 로봇이 새로 이동하는 위치 'R'로 표시
    return True


for cnt, direction in enumerate(move):
    if not move_jongsu_arduino(direction-1):
        print("kraj", cnt + 1) # cnt가 0부터 시작하므로 1 증가시켜서 출력
        exit(0)
    if not move_crazy_arduino():
        print("kraj", cnt + 1)
        exit(0)

for row in range(r):
    print(*board[row], sep='')