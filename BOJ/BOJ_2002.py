import sys
input = sys.stdin.readline
# [BOJ] 2002 추월 / 구현, 자료 구조, 문자열, 해시 사용 집합과 맵
n = int(input())
in_cars = {input().rstrip(): i for i in range(n)}
out_cars = [input().rstrip() for _ in range(n)]

answer = 0
for i in range(n-1):
    for j in range(i+1, n):
        if in_cars[out_cars[i]] > in_cars[out_cars[j]]:
            answer += 1
            break
print(answer)