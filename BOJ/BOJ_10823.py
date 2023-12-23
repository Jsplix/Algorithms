import sys
input = sys.stdin.readline
# [BOJ] 10823 더하기 2 / 수학, 문자열, 사칙연산, 파싱
# 빠른 입력 받을시 rstrip 때문인지 시간초과 발생.
s = ''
while True:
    try:
        s += input().rstrip()
    except:
        break
print(sum(map(int, s.split(','))))