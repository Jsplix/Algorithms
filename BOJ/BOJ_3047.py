import sys
input = sys.stdin.readline
# [BOJ] 3047 ABC / 구현
abc = sorted(map(int, input().split()))
seq = input().rstrip()

for s in seq:
    if s == 'A': print(abc[0], end=' ')
    elif s == 'B': print(abc[1], end=' ')
    else: print(abc[2], end=' ')