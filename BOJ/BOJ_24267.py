import sys
input = sys.stdin.readline
# [BOJ] 24267 알고리즘 수업 - 알고리즘의 수행 시간 6 / 구현
n = int(input())
print((n*(n-1)*(n-2))//6, 3, sep='\n')