import sys
input = sys.stdin.readline
# [BOJ] 30045 ZOAC 6 / 구현, 문자열
result = 0
for _ in range(int(input())):
    s = input().rstrip()
    result += 1 if s.count('01') or s.count('OI') else 0
print(result)