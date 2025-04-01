import sys
input = sys.stdin.readline
# [BOJ] 30236 증가 수열 / 그리디, 애드 혹
for _ in range(int(input())):
    n = int(input())
    nums = [i for i in range(1,n+1)]
    lst = list(map(int, input().split()))
    
    for i in range(len(nums)):
        if nums[i] == lst[i]:
            nums[i] += 1
    
        for j in range(i+1, len(nums)):
            if nums[j-1] >= nums[j]:
                nums[j] += (nums[j-1] - nums[j]) + 1
                
    print(nums[-1])