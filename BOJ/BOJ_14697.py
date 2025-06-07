import sys
input = sys.stdin.readline
# [BOJ] 14697 방 배정하기 / 브루트포스
a, b, c, n = map(int, input().split())

result = -1
flag = False
for i in range((n//a)+1):
    if a*i == n: 
        flag = True
        break
    for j in range((n//b)+1):
        if a*i + b*j == n: 
            flag = True
            break
        for k in range((n//c)+1):
            if a*i + b*j + c*k == n: 
                flag = True
                break

print(1 if flag else 0)