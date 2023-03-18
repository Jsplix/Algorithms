import sys
input = sys.stdin.readline
# [BOJ] 10825 국영수 / 정렬
n = int(input())
student = []
for _ in range(n):
    name, korean, english, mth = input().split()
    korean = int(korean)
    english = int(english)
    mth = int(mth)
    student.append((name, korean, english, mth))

student.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))
for i in range(n): print(student[i][0])