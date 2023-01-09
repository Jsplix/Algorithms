import sys
input = sys.stdin.readline
# [BOJ] 25325 학생 인기도 측정 / 자료 구조, 문자열, 정렬, 해시
n = int(input())
student_list = list(map(str, input().split()))
rank = {}
for student in student_list:
    rank[student] = 0

for i in range(n):
    name_list = list(map(str, input().split()))
    for name in name_list:
        rank[name] += 1

answer = list(zip(rank.keys(), rank.values()))
answer.sort(key=lambda x:-x[1])
for i in range(len(answer)):
    print(*answer[i])