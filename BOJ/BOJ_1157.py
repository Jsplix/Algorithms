import sys
input = sys.stdin.readline
# [BOJ] 1157 단어 공부 / 구현, 문자열
w = input().lower().rstrip()
char = {chr(i): 0 for i in range(ord('a'), ord('z')+1)}

for c in w:
    char[c] += 1

mx = max(char.values())
cnt, answer = 0, ''
for k in char.keys():
    if char[k] == mx: cnt += 1; answer = k.upper()

if cnt >= 2: print("?")
else: print(answer)