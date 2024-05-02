import sys
from collections import deque
input = sys.stdin.readline
# [BOJ] 31475 양갈래 배열 출력하기 / 구현
# 시작점 반환
def find_start(direction):
    global n, m
    if direction == 0: return (m//2, 0)
    elif direction == 1: return (m-1, n//2)
    elif direction == 2: return (m//2, n-1)
    elif direction == 3: return (0, n//2)

# 문자열 방향을 정수형으로 반환
def check(ch):
    if ch == 'U': return 0
    elif ch == 'R': return 1
    elif ch == 'D': return 2
    elif ch == 'L': return 3

# 배열 순회 함수
def traversal(sx, sy):
    global n, m, cnt, d
    queue = deque([(sx, sy, d, cnt)])
    while queue:
        x, y, dr, val = queue.popleft()
        arr[y][x] = val
        nx = x + dir[dr][0]
        ny = y + dir[dr][1]

        if 0 <= nx < m and 0 <= ny < n and not arr[ny][nx]:
            if (nx == 0) or (nx == m-1) or (ny == 0) or (ny == n-1):
                if (nx == 0 and dr == 1) or (nx == m-1 and dr == 3) or (ny == 0 and dr == 2) or (ny == n-1 and dr == 0):
                    queue.append((nx, ny, (dr+1)%4, val + 1))
                    queue.append((nx, ny, (dr-1)%4, val + 1))
                else:
                    queue.append((nx, ny, dr, val + 1))
            else:
                queue.append((nx, ny, dr, val + 1))
        elif 0 <= nx < m and 0 <= ny < n and arr[ny][nx]: # 방문한 칸을 가게 될 경우
            # 방향 바꾸고 갈 수 있는지 확인
            new_dr = (dr+1) % 4
            nnx = x + dir[new_dr][0]
            nny = y + dir[new_dr][1]
            if 0 <= nnx < m and 0 <= nny < n and not arr[nny][nnx]:
                queue.append((nnx, nny, new_dr, val + 1))

            # 방향 바꾸고 갈 수 있는지 확인
            new_dr = (dr-1) % 4
            nnx = x + dir[new_dr][0]
            nny = y + dir[new_dr][1]
            if 0 <= nnx < m and 0 <= nny < n and not arr[nny][nnx]:
                queue.append((nnx, nny, new_dr, val + 1))
    

n, m = map(int, input().split())
start = input().rstrip()

d = check(start)
# U: 0, R: 1, D: 2, L: 3
# 각각의 방향과 반대로 움직여야 함. ex) U일때는 아래 행으로 이동.
dir = {0: (0, 1), 1: (-1, 0), 2: (0, -1), 3: (1, 0)}
cnt = 1

arr = [[0 for _ in range(m)] for __ in range(n)]

fx, fy = find_start(d)
traversal(fx, fy)

for row in arr:
    print(*row)