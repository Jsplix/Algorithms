import sys
input = sys.stdin.readline
# [BOJ] 31994 강당 대관 / 구현
seminars = []
for _ in range(7):
    lecture, applications = input().split()
    applications = int(applications)
    seminars.append((lecture, applications))
seminars.sort(key=lambda x: x[1])

print(seminars[-1][0])