import sys
input = sys.stdin.readline
# [BOJ] 10798 세로 읽기 / 구현, 문자열
s = [list(input().rstrip()) for _ in range(5)]

answer = ''
idx = 0
max_len = -1

for i in range(5):
    max_len = max(max_len, len(s[i]))

for i in range(max_len):
    for j in range(5):
        if len(s[j]) > idx:
            answer += s[j][idx]
    idx += 1
print(answer)