from math import lcm
import sys
input = sys.stdin.readline
# [BOJ] 1145 적어도 대부분의 배수 / 브루트 포스
num = list(map(int, input().split()))
chk = []
for i in range(5):
    for j in range(5):
        if i == j: break
        for k in range(5):
            if k == i or k == j: break
            chk.append(lcm(num[i], num[j], num[k]))
print(min(chk))