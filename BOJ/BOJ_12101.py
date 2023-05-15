import sys
input = sys.stdin.readline
# [BOJ] 12101 1, 2, 3 더하기 2 / 브루트 포스, 백트래킹
n, k = map(int, input().split())
possible = []
num = [1, 2, 3]

def back(chk: list):
    if sum(chk) > n: return
    if sum(chk) == n:
        possible.append(chk[:])
        return

    for i in range(1, 4):
        chk.append(i)
        back(chk)
        chk.pop()

back([])
if len(possible) < k: print(-1)
else: print(*possible[k-1], sep='+')