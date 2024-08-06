import sys
input = sys.stdin.readline
# [BOJ] 15904 UCPC는 무엇의 약자일까? / 그리디, 문자열
s = input().rstrip()
d = {0: 'U', 1: 'C', 2: 'P', 3: 'C'}

idx = 0
for c in s:
    if idx == 4: break
    if c == d[idx]:
        idx += 1

if idx == 4:
    print("I love UCPC")
else:
    print("I hate UCPC")