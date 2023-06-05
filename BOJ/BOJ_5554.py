import sys
input = sys.stdin.readline
# [BOJ] 5554 심부름 가는 길 / 수학, 구현, 사칙연산
total_sec = 0
for _ in range(4):
    total_sec += int(input())

print(total_sec // 60, total_sec % 60, sep='\n')