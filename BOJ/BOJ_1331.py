import sys
input = sys.stdin.readline
# [BOJ] 1331 나이트 투어 / 구현, 시뮬레이션
row = {chr(i): i - ord('A') for i in range(ord('A'), ord('G'))}
visited = [[0 for _ in range(6)] for __ in range(6)]
path = list(input().rstrip() for _ in range(36))

flag = False
pr, pc = -1, -1
for p in path:
    r, c = int(p[1]) - 1, row[p[0]]

    if visited[r][c]:
        flag = True
        break

    visited[r][c] += 1
    
    if pr == -1 and pc == -1: 
        pr, pc = r, c
        continue

    if not ((abs(pr-r) == 1 and abs(pc-c) == 2) or (abs(pr-r) == 2 and abs(pc-c) == 1)):
        flag = True
        break

    pr, pc = r, c


sm = [sum(v) for v in visited]
if sum(sm) != 36: flag = True

sr, sc = int(path[0][1]) - 1, row[path[0][0]]
if not ((abs(sr-pr) == 1 and abs(sc-pc) == 2) or (abs(sr-pr) == 2 and abs(sc-pc) == 1)):
    flag = True 

if flag: print("Invalid")
else: print("Valid")