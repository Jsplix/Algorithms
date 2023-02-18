import sys
input = sys.stdin.readline
# [BOJ] 13414 수강신청 / 구현, 자료 구조, 해시를 사용한 집합과 맵
k, l = map(int, input().split())
wait = {}
for i in range(l):
    st_id = input().rstrip()
    wait[st_id] = i

answer = []
for key, val in wait.items():
    answer.append((key, val))
answer.sort(key=lambda x:x[1])

if len(answer) >= k:
    for i in range(k):
        print(answer[i][0])
else:
    for i in range(len(answer)):
        print(answer[i][0])