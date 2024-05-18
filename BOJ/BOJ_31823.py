import sys
input = sys.stdin.readline

n, m = map(int, input().split())
streak, who = [], []

for _ in range(n):
    *strk, name = input().split()
    streak.append(strk)
    who.append(name)

answer = []
for i in range(n):
    chk = 0
    flag = False
    for j in range(m):
        if streak[i][j] == '.':
            if flag: chk += 1
            else: chk = 1 ; flag = True
        else: flag = False
    answer.append(chk)

print(len(set(answer)))
for sr, nm in zip(answer, who):
    print(sr, nm)