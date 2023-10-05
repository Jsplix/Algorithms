import sys
input = sys.stdin.readline
# [BOJ] 25192 인사성 밝은 곰곰이 / 자료 구조, 해시 및 트리를 사용한 집합과 맵
cnt = 0
for _ in range(int(input())):
    history = input().rstrip()
    if history == 'ENTER':
        attendance = {}
    else:
        if history not in attendance.keys():
            attendance[history] = 1
            cnt += 1
        else:
            continue
print(cnt)