import sys
input = sys.stdin.readline
# [BOJ] 15922 아우으 우아으이야!! / 스위핑
n = int(input())
x, y = map(int, input().split())

answer = 0
for _ in range(n-1):
    nx, ny = map(int, input().split())

    if x <= ny <= y: continue
    elif x <= nx <= y and not x <= ny <= y:
        y = ny
    else:
        answer += abs(y-x)
        x, y = nx, ny

print(answer + abs(y-x))