import sys
input = sys.stdin.readline
# [BOJ] 11948 과목선택 / 수학, 구현, 사칙연산
s1 = []
for _ in range(4):
    s1.append(int(input()))

s2 = []
for _ in range(2):
    s2.append(int(input()))

s1.sort(reverse=True)
s2.sort(reverse=True)
print(sum(s1[:3]) + s2[0])