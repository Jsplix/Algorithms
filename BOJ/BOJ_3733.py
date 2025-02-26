import sys
input = sys.stdin.readline
# [BOJ] 3733 Shares / 수학, 사칙연산
while True:
    try:
        n, s = map(int, input().split())
        print(s//(n+1))
    except:
        break