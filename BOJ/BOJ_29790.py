import sys
input = sys.stdin.readline
# [BOJ] 29790 임스의 메이플컵 / 구현
n, u, l = map(int, input().split())
if n >= 1000 and (u >= 8000 or l >= 260):
    print("Very Good")
elif n >= 1000:
    print("Good")
else:
    print("Bad")