import sys
input = sys.stdin.readline
# [BOJ] 17588 Missing Numbers / 구현
nums = [int(input()) for _ in range(int(input()))]
result = []
for i in range(1, nums[-1]+1):
    if i not in nums:
        result.append(i)

if result: print(*result, sep='\n')
else: print("good job")