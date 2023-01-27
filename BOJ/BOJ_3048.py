import sys
input = sys.stdin.readline
# [BOJ] 3048 개미 / 문자열, 구현, 시뮬레이션
n1, n2 = map(int, input().split())
ant1 = input().rstrip()[::-1]
ant2 = input().rstrip()
t = int(input())

ant = ant1+ant2
p1 = len(ant1)-1
p2 = len(ant1)
ant = list(ant)

for _ in range(t):
    for i in range(len(ant)-1):
        if ant[i] in ant1 and ant[i + 1] in ant2: 
            ant[i], ant[i+1] = ant[i+1], ant[i]
            if ant[i+1] == ant1[-1]:
                break

print(''.join(ant))