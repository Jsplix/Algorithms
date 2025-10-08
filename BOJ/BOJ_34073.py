import sys
input = sys.stdin.readline
# [BOJ] 34073 DORO / 문자열
n = int(input())
s = list(input().split())
for word in s:
    word += 'DORO'
    print(word, end=" ")
print()