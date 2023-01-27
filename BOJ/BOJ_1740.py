import sys
input = sys.stdin.readline
# [BOJ] 1740 거듭제곱 / 비트마스킹, 수학
answer = []
n = int(input())

n_binary = bin(n)
n_binary = list(map(int, n_binary[2:]))
n_binary.reverse()

answer = 0

for i in range(len(n_binary)):
    if n_binary[i]:
        answer += 3**i
print(answer)

# n을 이진수로 변환하여 1인 부분의 index를 3의 지수로 올려서 계산해줌.
# 참고: https://pacific-ocean.tistory.com/246
# 이렇게 되면 중복되는 3의 제곱수 없이 최소합을 구할 수 있음.