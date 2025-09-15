import sys
input = sys.stdin.readline
# [BOJ] 10409 서버 / 수학, 구현, 사칙연산
n, t = map(int, input().split())
times = list(map(int, input().split()))

check = 0
count = 0
for time in times:
    check += time
    if check > t: break
    count += 1

print(count)