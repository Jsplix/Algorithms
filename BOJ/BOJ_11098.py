import sys
input = sys.stdin.readline
# [BOJ] 11098 첼시를 도와줘! / 구현, 문자열
for _ in range(int(input())):
    p = int(input())
    info = {}
    for i in range(p):
        price, name = input().split()
        price = int(price)
        info[name] = price
    print(sorted(info.items(), key=lambda x:x[1])[-1][0])