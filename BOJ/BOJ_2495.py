import sys
input = sys.stdin.readline
# [BOJ] 2495 연속구간 / 구현, 문자열
for _ in range(3):
    s = input().rstrip()
    result = 1
    mx = 1
    for i in range(7):
        if s[i] == s[i+1]:
            result += 1
        else:
            result = 1
        mx = max(mx, result)
    print(mx)