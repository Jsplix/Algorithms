import sys
input = sys.stdin.readline
# [BOJ] 1855 암호 / 구현, 문자열
k = int(input())
s = input().rstrip()

temp = [[] for _ in range(k)]
for i in range(len(s)):
    temp[i%k if (i // k) % 2 == 0 else k-1-(i%k)].append(s[i])

result = ''
for j in range(k):
    result += ''.join(temp[j])
print(result)