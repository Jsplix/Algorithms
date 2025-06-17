import sys
input = sys.stdin.readline
# [BOJ] 21966 (중략) / 구현, 문자열
n = int(input())
s = input().rstrip()

if n <= 25:
    print(s)
else:
    mid = s[11:-11]
    if '.' in mid:
        if mid.count('.') == 1 and mid[-1] == '.':
            print(s[:11] + '...' + s[-11:])
        else:
            print(s[:9] + '......' + s[-10:])
    else:
        print(s[:11] + '...' + s[-11:])