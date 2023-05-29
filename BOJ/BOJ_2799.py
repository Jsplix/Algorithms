import sys
input = sys.stdin.readline
# [BOJ] 2799 블라인드 / 구현
blind_type = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}

def check(x, y):
    window = []
    for r in range(x, x+4):
        s = ''
        for c in range(y, y+4):
            s += apart_info[r][c]
            checked[r][c] = 1
        window.append([s])
    
    if window == t1:
        blind_type[1] += 1
    elif window == t2:
        blind_type[2] += 1
    elif window == t3:
        blind_type[3] += 1
    elif window == t4:
        blind_type[4] += 1
    elif window == t5:
        blind_type[5] += 1

t1 = [['....'] for _ in range(4)]
t2 = [['****'], ['....'], ['....'], ['....']]
t3 = [['****'], ['****'], ['....'], ['....']]
t4 = [['****'], ['****'], ['****'], ['....']]
t5 = [['****'], ['****'], ['****'], ['****']]

m, n = map(int, input().split())
apart_info = [list(input().rstrip()) for _ in range(5*m+1)]

checked = [[0 for _ in range(5*n+1)] for _ in range(5*m+1)]

for i in range(5*m+1):
    for j in range(5*n+1):
        if apart_info[i][j] == '#': continue
        elif apart_info[i][j] == '.' and not checked[i][j]:
            check(i, j)
        elif apart_info[i][j] == '*' and not checked[i][j]:
            check(i, j)

print(*blind_type.values())