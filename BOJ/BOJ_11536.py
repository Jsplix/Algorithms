import sys
input = sys.stdin.readline
# [BOJ] 11536 줄 세우기 / 구현, 문자열, 정렬
li = [input().rstrip() for _ in range(int(input()))]
if li == sorted(li): print("INCREASING")
else:
    if li == sorted(li, reverse=True): print("DECREASING")
    else: print("NEITHER")