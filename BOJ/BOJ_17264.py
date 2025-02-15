import sys
from collections import defaultdict
input = sys.stdin.readline
# [BOJ] 17264 I AM IRONMAN / 구현, 자료 구조, 해시를 사용한 집합과 맵
n, p = map(int, input().split())
w, l, g = map(int, input().split())

players = defaultdict(int)
for _ in range(p):
    name, result = input().split()
    players[name] = w if result == 'W' else -l

flag = False
score = 0
for __ in range(n):
    nm = input().rstrip()
    if flag: continue
    if players[nm] == 0 or players[nm] == -l:
        score -= score if score - l < 0 else l
    else:
        score += players[nm]
    
    if score >= g: 
        flag = True

if not flag: print("I AM IRONMAN!!")
else: print("I AM NOT IRONMAN!!")