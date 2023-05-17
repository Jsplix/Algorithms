import sys
input = sys.stdin.readline
# [BOJ] 25496 장신구 명장 임스 / 그리디, 정렬
p, n = map(int, input().split())
a_list = list(map(int, input().split()))

a_list.sort()
answer, idx = 0, 0

for i in range(n):
    if p >= 200:
        break

    p += a_list[idx]
    idx += 1
    answer += 1
print(answer)