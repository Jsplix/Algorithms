import sys
input = sys.stdin.readline
# [BOJ] 17388 와글와글 숭고한 / 구현
p = list(map(int, input().split()))
if sum(p) >= 100:
    print("OK")
else:
    v = p.index(min(p))
    if v == 0: print("Soongsil")
    elif v == 1: print("Korea")
    else: print("Hanyang")