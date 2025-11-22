import sys
input = sys.stdin.readline
# [BOJ] 15784 질투진서 / 구현
N, A, B = map(int, input().split())
rooms = [list(map(int, input().split())) for _ in range(N)]

A -= 1
B -= 1
flag = False
X = rooms[A][B]
for i in range(N):
    if i == A: continue
    if rooms[i][B] > X:
        flag = True

for i in range(N):
    if i == B: continue
    if rooms[A][i] > X:
        flag = True

if flag: print("ANGRY")
else: print("HAPPY")