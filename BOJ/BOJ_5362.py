import sys
input = sys.stdin.readline
# [BOJ] 5362 Garbled Message / 구현, 문자열
for line in sys.stdin:
    line = line.rstrip()
    line = line.replace('iiing', 'th')
    print(line)