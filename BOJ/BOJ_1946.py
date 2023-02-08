import sys
input = sys.stdin.readline
# [BOJ] 1946 신입 사원 / 그리디 알고리즘, 정렬
for _ in range(int(input())):
    n = int(input())
    rank = [tuple(map(int, input().split())) for _ in range(n)]
    rank.sort()

    answer = 1
    s = 0
    for i in range(n):
        if rank[s][1] > rank[i][1]:
            answer += 1
            s = i
        
    print(answer)