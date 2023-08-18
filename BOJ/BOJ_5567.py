import sys
input = sys.stdin.readline
# [BOJ] 5567 결혼식 / 그래프 이론, 그래프 탐색
n = int(input())
f_list = [[] for _ in range(n+1)]
for _ in range(int(input())):
    a, b = map(int, input().split())
    f_list[a].append(b)
    f_list[b].append(a)

invite = [0 for _ in range(n+1)]
for f1 in f_list[1]:
    invite[f1] = 1
    for f2 in f_list[f1]:
        invite[f2] = 1

if invite[1] == 1: print(sum(invite) - 1)
else: print(sum(invite))