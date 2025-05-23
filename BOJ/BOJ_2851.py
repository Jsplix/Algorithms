import sys
input = sys.stdin.readline
# [BOJ] 2851 슈퍼 마리오 / 구현, 브루트포스, 누적 합
scores = [int(input()) for _ in range(10)]
result = scores[0]
gap = abs(result - 100)
for i in range(1, 10):
    if abs(result + scores[i] - 100) <= gap:
        result += scores[i]
        gap = abs(result - 100)
    else:
        break
print(result)