import sys
input = sys.stdin.readline
# [BOJ] 15917 노솔브 방지문제야!! / 수학, 구현
possible = set()
for i in range(31):
    possible.add(2**i)

for _ in range(int(input())):
    if int(input()) in possible: print(1)
    else: print(0)