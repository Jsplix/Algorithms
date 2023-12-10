import sys
input = sys.stdin.readline
# [BOJ] 1138 한 줄로 서기 / 구현
n = int(input())
arr = list(map(int, input().split())) # 왼쪽에 자기보다 키가 큰 사람이 몇 명인지
people = [0 for _ in range(n)] # 사람들이 현재 서 있는 상태

for i in range(n):
    chk = 0
    for j in range(n):
        if arr[i] == chk and people[j] == 0:
            people[j] = i + 1
            break
        elif people[j] == 0:
            chk += 1
print(*people)