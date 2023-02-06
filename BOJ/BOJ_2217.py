import sys
input = sys.stdin.readline
# [BOJ] 2217 로프 / 수학, 그리디, 정렬
rope = []
n = int(input())
for _ in range(n):
    rope.append(int(input()))
rope.sort() # 로프를 무게에 대해 오름차순 정렬
mx = n*min(rope) 
# 로프들 중 가벼운 무게의 로프를 1개씩 포기하며 최대 무게를 구함.
for i in range(1, n):
    mx = max(mx, (n-i)*rope[i])

print(mx)