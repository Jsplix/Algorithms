import sys
input = sys.stdin.readline
# [BOJ] 23812 골뱅이 찍기 - 돌아간 ㅍ / 구현
n = int(input())

for _ in range(n):
    print('@'*n + ' '*3*n + '@'*n)
for __ in range(n):
    print('@'*5*n)
for _ in range(n):
    print('@'*n + ' '*3*n + '@'*n)
for __ in range(n):
    print('@'*5*n)
for _ in range(n):
    print('@'*n + ' '*3*n + '@'*n)    