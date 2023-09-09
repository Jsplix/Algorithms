import sys
input = sys.stdin.readline
# [BOJ] 29791 에르다 노바와 오리진 스킬 / 구현, 정렬
n, m = map(int, input().split())
a = sorted(list(map(int, input().split())))
b = sorted(list(map(int, input().split())))

erda, ori = 1, 1
last = a[0]
for i in range(1, n):
    if last + 100 <= a[i]:
        last = a[i]
        erda += 1

last = b[0]
for i in range(1, m):
    if last + 360 <= b[i]:
        last = b[i]
        ori += 1

print(erda, ori)