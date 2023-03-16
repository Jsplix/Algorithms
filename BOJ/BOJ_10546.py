import sys
input = sys.stdin.readline
# [BOJ] 10546 배부른 마라토너 / 자료 구조, 해시 사용 집합과 맵
n = int(input())
attendance = {}
for _ in range(n):
    name = input().rstrip()
    if name in attendance.keys(): attendance[name] += 1
    else: attendance[name] = 1

for _ in range(n-1):
    runner = input().rstrip()
    attendance[runner] -= 1

li = sorted(list((attendance.items())), key=lambda x: -x[1])
print(li[0][0])