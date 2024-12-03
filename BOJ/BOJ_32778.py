import sys
input = sys.stdin.readline
# [BOJ] 32778 가희와 부역명 / 문자열, 파싱
name = input().rstrip()
temp = list(name.split())

main, sub = '', ''
flag = False
for c in name:
    if c == '(' or c == ')': 
        flag = True
        continue

    if not flag: main += c
    else: sub += c

if flag: print(main, sub, sep='\n')
else: print(main, "-", sep='\n')