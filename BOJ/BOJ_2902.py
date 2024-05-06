import sys
input = sys.stdin.readline
# [BOJ] 2902 KMP는 왜 KMP일까? / 구현, 문자열
long_name = list(input().rstrip().split('-'))
answer = ''
for name in long_name:
    answer += name[0]
print(answer)