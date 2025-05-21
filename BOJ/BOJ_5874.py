import sys
input = sys.stdin.readline
# [BOJ] 5874 소를 찾아라 / 누적 합, 스위핑
s = input().rstrip()
count, result = 0, 0
for i in range(1, len(s)-1):
    if s[i] == '(' and s[i-1] == '(': count += 1
    if s[i] == ')' and s[i+1] == ')': result += count
print(result)