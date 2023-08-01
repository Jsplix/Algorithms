import sys
input = sys.stdin.readline
# [BOJ] 13909 창문 닫기 / 수학, 정수론
# 창문이 열려있기 위해서는 해당수는 제곱수여야 함. (약수가 홀수개 있어야하므로)
n = int(input())
x = 1
answer = 0
while x**2 <= n:
    answer += 1
    x += 1
print(answer)