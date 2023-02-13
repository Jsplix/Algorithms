import sys
input = sys.stdin.readline
# [BOJ] 1032 명령 프롬프트 / 구현, 문자열
n = int(input())
cmd = [input().rstrip() for _ in range(n)]

chk = []
if n == 1: 
    print(cmd[0])
    exit(0)
else:
    for i in range(n):
        for j in range(i+1, n):
            for k in range(len(cmd[0])):
                if i == 0 and j == 1:
                    if cmd[i][k] == cmd[j][k]:
                        chk.append(cmd[i][k])
                    else:
                        chk.append('?')
                else:
                    if cmd[i][k] != cmd[j][k]:
                        chk[k] = '?'

print(''.join(chk))