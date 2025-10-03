import sys
input = sys.stdin.readline
# [BOJ] 34553 알파벳 점수 계산기 / 구현, 문자열
s = input().rstrip()
total = 1
now = 1

prev = s[0]
for i in range(1, len(s)):
    if prev < s[i]: 
        now += 1
        total += now
    else:
        now = 1
        total += now
    prev = s[i]
print(total)