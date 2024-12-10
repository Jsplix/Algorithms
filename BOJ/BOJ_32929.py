import sys
input = sys.stdin.readline
# [BOJ] 32929 UOS 문자열 / 수학, 구현, 문자열, 사칙연산
n = int(input())
answer = {1: 'U', 2: 'O', 0: 'S'}
print(answer[n%3])