import sys
input = sys.stdin.readline
# [BOJ] 22251 빌런 호석 / 구현, 브루트포스
def dfs(floor, t_cnt, possible: str):
    global n, x
    if floor >= len(possible):
        if int(possible) == x: return 0
        elif 1 <= int(possible) <= n: return 1
        else: return 0
    
    chk, now = 0, int(possible[floor])
    for i in range(10):
        if now != i and diff[now][i] <= t_cnt:
            px = possible[:floor] + str(i) + possible[floor+1:]
            chk += dfs(floor+1, t_cnt-diff[now][i], px)
        elif now == i:
            chk += dfs(floor+1, t_cnt, possible)

    return chk

leds = {0: '1111110', 1: '0110000', 2: '1101101', 3: '1111001', 4: '0110011', 5: '1011011', 6: '1011111', 7: '1110000', 8: '1111111', 9: '1111011'}
n, k, p, x = map(int, input().split())
diff = []

for i in range(10):
    diff.append([])
    for j in range(10):
        if i == j: diff[i].append(0)
        else:
            chk = 0
            for b in range(7):
                if leds[i][b] != leds[j][b]: chk += 1
            diff[i].append(chk)

nx = str(x)
if len(nx) != k:
    nx = '0'*(k-len(nx)) + nx

print(dfs(0, p, nx))