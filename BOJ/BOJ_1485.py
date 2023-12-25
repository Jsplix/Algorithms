import sys
input = sys.stdin.readline
# [BOJ] 1485 정사각형 / 정렬, 기하학
def solve(p1: tuple, p2: tuple):
    return (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2

for _ in range(int(input())):
    pos = [tuple(map(int, input().split())) for __ in range(4)]
    pos.sort(key=lambda x:(x[0], x[1]))
    dist = [solve(pos[0], pos[1]), solve(pos[0], pos[2]), solve(pos[0], pos[3]),
            solve(pos[1], pos[2]), solve(pos[1], pos[3]), solve(pos[2], pos[3])]
    
    if dist.count(max(dist)) == 2 and dist.count(min(dist)) == 4: print(1)
    else: print(0)