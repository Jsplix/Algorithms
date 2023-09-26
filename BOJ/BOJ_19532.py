import sys
input = sys.stdin.readline
# [BOJ] 19532 수학은 비대면강의입니다 / 수학, 브루트포스
var = list(map(int, input().split()))

for i in range(-999, 1000):
    for j in range(-999, 1000):
        if var[0]*i + var[1]*j == var[2] and var[3]*i + var[4]*j == var[5]:
            print(i, j)
            exit(0)