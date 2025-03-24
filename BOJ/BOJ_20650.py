import sys
input = sys.stdin.readline
# [BOJ] 20650 Do You Know Your ABCs? / 수학, 브루트포스, 정렬
nums = list(map(int, input().split()))
nums.sort()

for i in range(7):
    for j in range(7):
        if j == i: continue
        for k in range(7):
            if k == j or k == i: continue
            temp = sorted([nums[i], nums[j], nums[k], nums[i]+nums[j], nums[j]+nums[k], nums[k]+nums[i], nums[i]+nums[j]+nums[k]])
            if temp == nums:
                print(nums[i], nums[j], nums[k])
                exit(0)