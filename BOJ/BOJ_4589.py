import sys
input = sys.stdin.readline
# [BOJ] 4589 Gnome Sequencing / 구현
result = []
for _ in range(int(input())):
    temp = list(map(int, input().split()))
    if temp == sorted(temp) or temp == sorted(temp, reverse=True):
        result.append("Ordered")
    else:
        result.append("Unordered")

print("Gnomes:")
print(*result, sep='\n')