import sys
input = sys.stdin.readline
# [BOJ] 18311 왕복 / 구현
n, k = map(int, input().split())
course = list(map(int, input().split()))
course = course + course[::-1]

for i in range(2*n):
    k -= course[i]
    if k < 0:
        if i > n:
            print((2*n) - i)
            break
        else:
            print(i+1)
            break