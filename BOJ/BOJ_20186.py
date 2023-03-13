import sys
input = sys.stdin.readline
# [BOJ] 20186 수 고르기 / 수학, 그리디, 정렬
n, k = map(int, input().split())
arr = sorted(list(map(int, input().split())), reverse=True)
answer = arr[0]
for i in range(1, k):
    answer += (arr[i]-i)
print(answer)