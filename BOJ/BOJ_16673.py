import sys
input = sys.stdin.readline
# [BOJ] 16673 고려대학교에는 공식 와인이 있다 / 수학, 사칙연산
c, k, p = map(int, input().split())
total = 0
for i in range(1, c+1):
    total += ((k * i) + (p * i ** 2))
print(total)