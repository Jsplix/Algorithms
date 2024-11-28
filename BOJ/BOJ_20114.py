import sys
input = sys.stdin.readline
# [BOJ] 20114 미아 노트 / 문자열
n, h, w = map(int, input().split())
patterns = [list(input().rstrip()) for _ in range(h)]

answer = ''
for i in range(n):
    temp = '?'
    for j in range(h):
        for k in range(i*w, (i+1)*w):
            if patterns[j][k] != '?':
                temp = patterns[j][k]
    answer += temp
print(answer)