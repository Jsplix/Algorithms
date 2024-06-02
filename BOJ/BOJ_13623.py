import sys
input = sys.stdin.readline
# [BOJ] 13623 Zero or One / 구현
inp = list(map(int, input().split()))
who = {0: 'A', 1: 'B', 2: 'C'}
sm = sum(inp)
if sm == 3: print('*')
elif sm == 2: print(who[inp.index(0)])
elif sm == 1: print(who[inp.index(1)])
else: print('*')