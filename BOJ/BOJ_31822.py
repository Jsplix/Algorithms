import sys
input = sys.stdin.readline
# [BOJ] 31822 재수강 / 구현, 문자열
subject_code = input().rstrip()
n = int(input())
answer = 0
for _ in range(n):
    subject = input().rstrip()
    if subject[:5] == subject_code[:5]:
        answer += 1
print(answer)