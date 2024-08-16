import sys
input = sys.stdin.readline
# [BOJ] 30642 아이그루스와 화장실 / 수학, 구현, 사칙연산
n = int(input())
character = input().rstrip()
k = int(input())

if character == "annyong":
    if k % 2: print(k)
    else: print(k-1)
else:
    if k % 2 and k != 1: print(k-1)
    elif k == 1: print(k+1)
    else: print(k)