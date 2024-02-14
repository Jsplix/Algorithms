import sys
input = sys.stdin.readline
# [BOJ] 14499 주사위 굴리기 / 구현, 시뮬레이션
def move_north(x, y): # 기존의 북쪽면 -> 밑면, 밑면 -> 남쪽면, 남쪽면 -> 윗면, 윗면 -> 북쪽면
    if 0 <= x < m and 0 <= y < n:
        temp = dice[2]          # 기존의 북쪽면 복사
        dice[2] = dice[6]       # 북쪽면 -> 밑면
        dice[6] = dice[5]       # 밑면 -> 남쪽면
        dice[5] = dice[1]       # 남쪽면 -> 윗면
        dice[1] = temp          # 윗면 -> 북쪽면

        if graph[y][x] == 0: graph[y][x] = dice[6]
        else: dice[6] = graph[y][x] ; graph[y][x] = 0
        return dice[1]
    else:
        return -1

def move_south(x, y): # 기존의 남쪽면 -> 밑면, 밑면 -> 북쪽면, 북쪽면 -> 윗면, 윗면 -> 남쪽면
    if 0 <= x < m and 0 <= y < n:
        temp = dice[5]          # 기존의 남쪽면 복사
        dice[5] = dice[6]       # 남쪽면 -> 밑면
        dice[6] = dice[2]       # 밑면 -> 북쪽면
        dice[2] = dice[1]       # 북쪽면 -> 윗면
        dice[1] = temp          # 윗면 -> 남쪽면

        if graph[y][x] == 0: graph[y][x] = dice[6]
        else: dice[6] = graph[y][x] ; graph[y][x] = 0
        return dice[1]
    else:
        return -1

def move_west(x, y): # 기존의 윗면 -> 동쪽면, 동쪽면 -> 밑면, 밑면 -> 서쪽면, 서쪽면 -> 윗면
    if 0 <= x < m and 0 <= y < n:
        temp = dice[1]
        dice[1] = dice[3]
        dice[3] = dice[6]
        dice[6] = dice[4]
        dice[4] = temp

        if graph[y][x] == 0: graph[y][x] = dice[6]
        else: dice[6] = graph[y][x] ; graph[y][x] = dice[6] ; graph[y][x] = 0
        return dice[1]
    else:
        return -1

def move_east(x, y): # 기존의 윗면 -> 서쪽면, 서쪽면 -> 밑면, 밑면 -> 동쪽면, 동쪽면 -> 윗면
    if 0 <= x < m and 0 <= y < n:
        temp = dice[1]
        dice[1] = dice[4]
        dice[4] = dice[6]
        dice[6] = dice[3]
        dice[3] = temp

        if graph[y][x] == 0: graph[y][x] = dice[6]
        else: dice[6] = graph[y][x] ; graph[y][x] = dice[6] ; graph[y][x] = 0
        return dice[1]
    else:
        return -1

n, m, y, x, k = map(int, input().split())
graph = [ list(map(int, input().split())) for _ in range(n) ]
commands = list(map(int, input().split()))

# 이동한 칸에 쓰인 수가 0 -> 주사위 바닥면의 수가 복사됨.
# 0이 아닌 경우 -> 칸에 쓰인 수가 주사위의 바닥면으로 복사됨.

# 주사위가 서쪽, 동쪽으로 움직일 경우 밑면이 반대쪽 옆면이 되고 기존의 옆면은 윗면이 됨.
# ex) 밑면 6, 윗면 1, 동쪽면 3 일 때, 동쪽으로 이동 --> 밑면 3, 서쪽면, 6, 동쪽면 1이 됨.

# 문제의 전개도와 동일하게 취급.
dice = {i: 0 for i in range(1, 7)} 
for comm in commands:
    ret = -1
    if comm == 1: 
        if 0 <= x + 1 < m and 0 <= y < n:
            x += 1
            ret = move_east(x, y)
    elif comm == 2:
        if 0 <= x - 1 < m and 0 <= y < n:
            x -= 1
            ret = move_west(x, y)
    elif comm == 3:
        if 0 <= x < m and 0 <= y - 1 < n:
            y -= 1
            ret = move_north(x, y)
    elif comm == 4:
        if 0 <= x < m and 0 <= y + 1 < n:
            y += 1
            ret = move_south(x, y)
    if ret == -1: continue
    else: print(ret)