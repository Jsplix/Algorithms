import sys
input = sys.stdin.readline
# [BOJ] 3980 선발 명단 / 브루트포스, 백트래킹
def back(idx, val):
    global answer
    if idx == 11:
        answer = max(answer, val)
        return
    
    for i in range(11):
        if not selected[i] and stats[idx][i]:
            selected[i] = 1
            back(idx + 1, val + stats[idx][i])
            selected[i] = 0

for _ in range(int(input())):
    stats = [list(map(int, input().split())) for _ in range(11)]

    selected = [0 for _ in range(11)]
    answer = 0

    back(0, 0)
    print(answer)