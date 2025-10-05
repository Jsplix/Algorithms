import sys
input = sys.stdin.readline
# [BOJ] 1016 제곱 ㄴㄴ수 / 수학, 정수론, 소수 판정, 에라토스테네스의 체
LIM = 10**6 + 7
mn, mx = map(int, input().split())
result = mx - mn + 1

e = [0 for _ in range(LIM)]
for i in range(2, int(mx**0.5 + 1)):
    sq = i ** 2
    for j in range((((mn - 1) // sq) + 1) * sq, mx + 1, sq):
        if not e[j - mn]:
            e[j - mn] = 1
            result -= 1

print(result)