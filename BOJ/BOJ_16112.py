import sys
input = sys.stdin.readline
# [BOJ] 16112 5차 전직 / 정렬, 그리디
n, k = map(int, input().split())
exp = list(map(int, input().split()))

exp.sort()
active = 0 # 활성화 된 돌의 개수
result = 0 # 최종적으로 획득한 경험치

for i in range(n):
    result += active * exp[i]
    if active < k:
        active += 1
print(result)