import sys
input = sys.stdin.readline
# [BOJ] 2693 N번째 큰 수 / 정렬
for _ in range(int(input())):
    print(sorted(map(int, input().split()))[-3])