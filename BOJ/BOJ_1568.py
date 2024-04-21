import sys
input = sys.stdin.readline
# [BOJ] 1568 새 / 수학, 구현
n = int(input())
now = n
cnt = 0
bird = 1
while bird <= now:
    now -= bird
    bird += 1
    cnt += 1
    if bird > now:
        bird = 1
    
print(cnt)