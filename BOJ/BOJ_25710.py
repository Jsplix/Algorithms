import sys
input = sys.stdin.readline
# [BOJ] 25710 점수 계산 / 브루트 포스
n = int(input())
l = list(map(int, input().split()))
chk = [0 for _ in range(1000)]

for x in l:
    chk[x] += 1

num_list = []

for i in range(1, 1000):
    if chk[i] == 1:
        num_list.append(i)
    elif chk[i] >= 2:
        num_list.append(i)
        num_list.append(i)

ans = []

for i in range(len(num_list)):
    for j in range(i + 1, len(num_list)):
        temp = num_list[i] * num_list[j]
        ans.append(sum(list(map(int, str(temp)))))

print(max(ans))