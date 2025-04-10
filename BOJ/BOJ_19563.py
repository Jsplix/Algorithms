import sys
input = sys.stdin.readline
# [BOJ] 19563 개구리 1 / 수학
a, b, c = map(int, input().split())
# 바로 c로 가는 경우 + 다른 곳을 거쳐서 오는 경우
c -= abs(a) + abs(b)
print("YES" if c % 2 == 0 and not c < 0 else "NO")