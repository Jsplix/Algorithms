import sys
input = sys.stdin.readline
# [BOJ] 11659 구간 합 구하기 4 / 누적 합
n, m = map(int, input().split())
l = list(map(int, input().split()))
for x in range(1, len(l)):
    l[x] += l[x - 1] # 입력을 받음과 동시에 누적 합을 구해줌
for _ in range(m): 
    i, j = map(int, input().split())
    if i == j and i != 1: # 입력된 i, j값을 기준으로 빼주기만 하면 됨(합은 위에서 구했기 때문)
        print(l[j - 1] - l[i - 2])
    elif i == 1:
        print(l[j - 1])
    else:
        print(l[j - 1] - l[i - 2])