import sys
input = sys.stdin.readline
# [BOJ] 2857 FBI / 구현, 문자열
count = []
for i in range(1, 6):
    name = input().rstrip()
    if 'FBI' in name:
        count.append(i)

if count: print(*count)
else: print("HE GOT AWAY!")