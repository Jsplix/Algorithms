import sys
input = sys.stdin.readline
# [BOJ] 1547 공 / 구현, 시뮬레이션
cup = ['1', '2', '3']
for _ in range(int(input())):
    a, b = map(int, input().split())
    cup[a-1], cup[b-1] = cup[b-1], cup[a-1]
print(cup.index('1')+1)