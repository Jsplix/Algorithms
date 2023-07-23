import sys
input = sys.stdin.readline
# [BOJ] 11558 The Game of Death / 구현, 그래프 이론, 그래프 탐색, 시뮬레이션
rec = []
def call(num):
    global n, t
    if players[num] == n:
        print(t)
        return
    else:
        if players[players[num]] in rec:
            print(0)
        else:
            rec.append(players[num])
            t += 1
            call(players[num])

for _ in range(int(input())):
    n = int(input())
    players = [0] + [int(input()) for _ in range(n)]
    t = 1
    if n not in players: print(0)
    else:
        rec.append(players[1])
        call(1)