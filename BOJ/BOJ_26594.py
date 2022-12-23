import sys
input = sys.stdin.readline
# [BOJ] 26594 ZOAC 5 / 구현, 문자열
s = input().rstrip()
chk = 1
for i in range(len(s) - 1):
    if s[i] != s[i + 1]:
        break
    chk += 1
print(chk)