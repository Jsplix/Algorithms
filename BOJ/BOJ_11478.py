import sys
input = sys.stdin.readline
# [BOJ] 11478 서로 다른 부분 문자열의 개수 / 자료 구조, 문자열
s = input().rstrip()
ans = []
for i in range(len(s)):
    for j in range(i, len(s)):
        ans.append(s[i:j + 1])
print(len(set(ans)))