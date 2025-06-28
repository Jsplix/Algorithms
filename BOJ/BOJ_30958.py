import sys
input = sys.stdin.readline
# [BOJ] 30958 서울사이버대학을 다니고 / 구현, 문자열
count = {chr(i): 0 for i in range(ord('a'), ord('z')+1)}

n = int(input())
logosong = input().rstrip()
for c in logosong:
    if c == ' ' or c == ',' or c == '.':
        continue
    count[c] += 1

print(sorted(count.items(), key=lambda x:-x[1])[0][1])