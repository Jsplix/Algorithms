import sys
input = sys.stdin.readline
# [BOJ] 22862 가장 긴 짝수 연속한 부분 수열 (large) / 투 포인터
n, k = map(int, input().split())
s = list(map(int, input().split()))

odd, count = 0, 0
end = 0
result = 0
for start in range(n):
    while odd <= k and end < n:
        if s[end] % 2: odd += 1
        else: count += 1

        if start == 0 and end == n:
            result = count
            break
        end += 1

    result = max(result, count)
    if s[start] % 2: odd -= 1
    else: count -= 1

print(result)