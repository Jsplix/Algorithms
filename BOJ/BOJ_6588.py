import sys
import math
input = sys.stdin.readline
# [BOJ] 6588 골드바흐의 추측 / 수학, 정수론, 소수 판정, 에라토스테네스의 체
n = [0, 1]
chk = []
id = 2

max_num = n[0]
while True: 
    n.append(int(input()))
    id += 1
    if n[id - 1] == 0:
        n.pop()
        break
    if n[id - 1] > max_num:
        max_num = n[id - 1]

Erathsthenes = [ x for x in range(max_num + 1) ]

for i in range(2, int((max_num)**0.5)+1):
    if Erathsthenes[i] == 0:
        continue
    for j in range(i + i, max_num + 1, i):
        Erathsthenes[j] = 0

id = 2
l = 2

while id != len(n):
    if Erathsthenes[n[id] - Erathsthenes[l]]:
        chk.append(Erathsthenes[l])
        chk.append(n[id] - Erathsthenes[l])
        id += 1
        l = 2
    else:
        l += 1

x = 0

for k in range(2, len(n)):
    print(str(n[k]) + " = " + str(chk[x]) + " + " + str(chk[x + 1]))
    x += 2