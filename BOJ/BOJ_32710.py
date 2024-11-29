import sys
input = sys.stdin.readline
# [BOJ] 32710 구구단표 / 수학, 구현, 브루트포스, 사칙연산
n = int(input())
flag = False
for i in range(2, 10):
    if i == n: 
        flag = True
        break
    for j in range(1, 10):
        if j == n: 
            flag = True
            break
        if i * j == n: flag = True

    if flag: break

if flag: print(1)
else: print(0)