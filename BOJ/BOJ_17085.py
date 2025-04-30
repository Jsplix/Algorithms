import sys
input = sys.stdin.readline
# [BOJ] 17085 십자가 2개 놓기 / 구현, 브루트포스
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def get_size(y, x):
    global n, m, size

    for i in range(size, 0, -1):
        check = 1
        for d in range(i, 0, -1):
            for r in range(4):
                nx = x + d * dx[r]
                ny = y + d * dy[r]

                if 0 <= nx < m and 0 <= ny < n and boards[ny][nx] == '#':
                    check += 1
        
        if check == 4*i + 1:
            return i
    
    return 0

def get_positions(y, x, sz):
    ret = set()
    for i in range(y-sz, y+sz+1):
        ret.add((i, x))
    for j in range(x-sz, x+sz+1):
        ret.add((y, j))
    return ret

def is_duplicated(y1, x1, sz1, y2, x2, sz2):
    p1 = get_positions(y1, x1, sz1)
    p2 = get_positions(y2, x2, sz2)

    if p1.intersection(p2):
        return True
    
    return False


n, m = map(int, input().split())
boards = [list(input().rstrip()) for _ in range(n)]

mn = min(n, m)
size = mn // 2 if mn % 2 else (mn-1) // 2

possible = []
for i in range(n):
    for j in range(m):
        if boards[i][j] == '#':
            temp = get_size(i, j)
            for t in range(temp+1):
                possible.append((i, j, t)) # y, x, size
possible.sort(key=lambda x:-x[2])

result = 1
for f in range(len(possible)):
    for s in range(f+1, len(possible)):
        if not is_duplicated(possible[f][0], possible[f][1], possible[f][2], possible[s][0], possible[s][1], possible[s][2]):
            area1 = 4*possible[f][2] + 1
            area2 = 4*possible[s][2] + 1

            result = max(result, area1*area2)
print(result)