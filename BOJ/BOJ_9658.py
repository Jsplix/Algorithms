import sys
input = sys.stdin.readline
# [BOJ] 9658 돌 게임 4 / DP, 게임 이론
# 상근이 이기는 경우 - 1, 창영이가 게임을 이기는 경우 - 0
winner = [0, 0, 1, 0, 1] + [0 for _ in range(1000)]

n = int(input())

if n >= 5:
    for i in range(5, 1001):
        if winner[i-1] and winner[i-3] and winner[i-4]: winner[i] = 0
        else: winner[i] = 1

if winner[n]: print("SK")
else: print("CY")