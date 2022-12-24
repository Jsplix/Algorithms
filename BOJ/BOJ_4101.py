import sys
input = sys.stdin.readline
# [BOJ] 4101 크냐? / 구현
while True:
    a, b = map(int, input().split())
    if a == b == 0:
        break
    print("Yes" if a > b else "No")