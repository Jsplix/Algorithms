import sys
input = sys.stdin.readline
# [BOJ] 12927 배수 스위치 / 그리디
bulb = list(map(str, input().rstrip()))
cnt = 0
n = len(bulb)
# i를 기준으로 이미 껐던 전구는 다시 켜지지 않음 (배수만 반전되므로)
# 따라서, 전구가 모두 안꺼질 일은 발생할 수 없음.
for i in range(n):
    if bulb[i] == 'Y':
        cnt += 1
        for j in range(i, n, i+1):
            if bulb[j] == 'N': bulb[j] = 'Y'
            else: bulb[j] = 'N'

print(cnt)