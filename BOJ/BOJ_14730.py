import sys
input = sys.stdin.readline
# [BOJ] 14730 謎紛芥索紀 (Small) / 수학, 미분적분학
n = int(input())

k_list, c_list  = [], []
for _ in range(n):
    c, k = map(int, input().split())
    c_list.append(c)
    k_list.append(k)

t_list = [0 for _ in range(n)]
for i in range(n):
    t_list[i] = c_list[i] * k_list[i]
    k_list[i] -= 1

print(sum(t_list))