import sys
input = sys.stdin.readline
# [BOJ] 1526 가장 큰 금민수 / 구현, 수학, 브루트포스
x = ['0', '1', '2', '3', '5', '6', '8', '9']
n = int(input())
while True:
    sn = str(n)
    flag = False
    for k in x:
        if k in sn:
            flag = True
            n -= 1
            break
    if not flag:
        print(n)
        break