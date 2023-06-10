import sys
input = sys.stdin.readline
# [BOJ] 2910 빈도 정렬 / 자료 구조, 정렬, 해시 사용 집합과 맵
n, c = map(int, input().split())
arr = list(map(int, input().split()))

num_dict = {} # 빈도

for i in range(n):
    if arr[i] not in num_dict.keys():
        num_dict[arr[i]] = [1, i]
    else:
        num_dict[arr[i]][0] += 1

check = []
for k, v in num_dict.items():
    check.append((k, *v))
check.sort(key=lambda x:(-x[1], x[2]))

for i in range(len(check)):
    for j in range(check[i][1]):
        print(check[i][0], end = ' ')