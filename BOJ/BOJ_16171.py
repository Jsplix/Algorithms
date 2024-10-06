import sys
input = sys.stdin.readline
# [BOJ] 16171 나는 친구가 적다 (Small) / 문자열
s = input().rstrip()
answer = input().rstrip()

temp = ''
for c in s:
    if c.isnumeric():
        continue
    else:
        temp += c

print(1 if temp.find(answer) != -1 else 0)