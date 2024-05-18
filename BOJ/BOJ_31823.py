import sys
input = sys.stdin.readline
# [BOJ] 31823 악질 검거 / 구현
n, m = map(int, input().split())
streak, who = [], []

for _ in range(n):
    *strk, name = input().split()
    streak.append(strk)
    who.append(name)

answer = []
for i in range(n):
    chk = 0
    mx = 0
    flag = False
    for j in range(m):
        if streak[i][j] == '.':
            if flag: chk += 1
            else: chk = 1 ; flag = True
        else: 
            if chk:
                mx = max(mx, chk)
                chk = 0
            flag = False
    mx = max(mx, chk)

    answer.append(mx)

print(len(set(answer)))
for sr, nm in zip(answer, who):
    print(sr, nm)