import sys
input = sys.stdin.readline
# [BOJ] 31518 Triple Sevens / 구현
n = int(input())
flag = False
for i in range(3):
    x = list(map(int, input().split()))
    if 7 not in x: flag = True
print(0 if flag else 777)