import sys
input = sys.stdin.readline
# [BOJ] 24265 알고리즘 수업 - 알고리즘의 수행 시간 4 / 수학, 구현
n = int(input())
print((n*(n-1))//2, 2, sep='\n')