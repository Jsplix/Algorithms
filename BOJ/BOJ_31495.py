import sys
input = sys.stdin.readline
# [BOJ] 31495 그게 무슨 코드니.. / 구현, 문자열
s = input().rstrip()
chk = s.count('"')
if chk == 1: print("CE")
elif chk == 2: 
    if s[0] == '"' and s[-1] == '"':
        print("CE" if len(s[1:-1]) == 0 else s[1:-1])
    else:
        print("CE")
elif chk == 0: print("CE")