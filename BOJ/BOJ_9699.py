import sys
input = sys.stdin.readline
# [BOJ] 9699 RICE SACK / 구현
for i in range(1, int(input())+1):
    temp = list(map(int, input().split()))
    print("Case #%d:" %i, max(temp))