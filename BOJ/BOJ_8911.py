import sys
input = sys.stdin.readline

# [BOJ] 8911 거북이 / 구현, 시뮬레이션

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

for _ in range(int(input())):
    op = input().rstrip()
    direction = 3 # 현재 방향, 처음에는 북쪽을 보고있음
    x, y = 0, 0
    max_x, max_y, min_x, min_y = 0, 0, 0, 0
    # 0 - 서 / 1 - 남 / 2 - 동 / 3 - 북 -> 반시계 방향
    for c in op:
        if c == 'F':
            x += dx[direction]
            y += dy[direction]

        elif c == 'B':
            x -= dx[direction]
            y -= dy[direction]
        
        elif c == 'L':
            if direction == 3: direction = 0
            else: direction += 1
        
        elif c == 'R':
            if direction == 0: direction = 3
            else: direction -= 1

        max_x = max(max_x, x)
        max_y = max(max_y, y)
        min_x = min(min_x, x)
        min_y = min(min_y, y)

    w = abs(max_x-min_x)
    h = abs(max_y-min_y)
    print(w*h)