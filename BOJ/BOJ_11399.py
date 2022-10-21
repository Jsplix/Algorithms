import sys
input = sys.stdin.readline

n = int(input())
sp_time = list(map(int, input().split()))
sp_time.sort()
total = [0 for _ in range(n)]
total[0] = sp_time[0]
for i in range(1, n):
    total[i] = total[i - 1] + sp_time[i]
print(sum(total))