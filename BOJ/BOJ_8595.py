import sys
input = sys.stdin.readline
# [BOJ] 8595 히든 넘버 / 문자열, 파싱
n = int(input())
s = input().rstrip()

temp = ''
result = 0
for i in range(n):
    if s[i].isnumeric():
        temp += s[i]
    else:
        if len(temp): 
            result += int(temp)
            temp = ''

if len(temp): result += int(temp)
print(result)