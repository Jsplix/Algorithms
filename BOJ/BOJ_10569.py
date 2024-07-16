import sys
input = sys.stdin.readline
# [BOJ] 10569 다면체 / 수학, 기하학, 사칙연산, 오일러 지표(χ=v-e+f)
for _ in range(int(input())):
    v, e = map(int, input().split())
    print(2-v+e)