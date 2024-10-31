import sys
input = sys.stdin.readline
# [BOJ] 14405 피카츄 / 문자열
S = input().rstrip()
for word in ["pi", "ka", "chu"]:
    S = S.replace(word, '*')

if S.replace('*', '') == '': print("YES")
else: print("NO")