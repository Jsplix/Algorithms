import sys
input = sys.stdin.readline
# [BOJ] 2587 대표값2 / 수학, 구현, 정렬
l = []
for i in range(5):
    l.append(int(input()))

l.sort()
print(sum(l) // 5)
print(l[2])