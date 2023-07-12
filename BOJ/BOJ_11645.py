import sys
input = sys.stdin.readline
# [BOJ] 11645 I've Been Everywhere, Man / 자료 구조, 문자열, 해시
for _ in range(int(input())):
    n = int(input())
    d = {}
    for i in range(n):
        s = input().rstrip()
        d[s] = 1
    print(len(list(d.keys())))