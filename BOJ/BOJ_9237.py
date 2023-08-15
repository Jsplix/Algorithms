import sys
input = sys.stdin.readline
# [BOJ] 9237 이장님의 초대 / 그리디, 정렬
n = int(input())
trees = sorted(list(map(int, input().split())), reverse=True)

for i in range(n):
    trees[i] += i + 2
print(max(trees))