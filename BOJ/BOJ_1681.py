import sys
input = sys.stdin.readline
# [BOJ] 1681 줄 세우기 / 구현, 브루트포스
N, L = map(int, input().split())

mx = 0
L = str(L)

now = 0
cnt = 0
while True:
    now += 1
    cnt += 1
    if L in str(now):
        cnt -= 1
        continue
    
    if cnt == N: break
print(now)