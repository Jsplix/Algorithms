import sys
input = sys.stdin.readline
# [BOJ] 10174 팰린드롬 / 구현, 문자열
for _ in range(int(input())):
    s = input().strip()
    s = s.lower()
    if s == s[::-1]: print("Yes")
    else: print("No")