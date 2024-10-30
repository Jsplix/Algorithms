import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline
# [BOJ] 24460 특별상이라도 받고 싶어 / 분할 정복, 재귀
def solve(size, r, c):
    if size == 2:
        temp = sorted([nums[r][c], nums[r][c+1], nums[r+1][c], nums[r+1][c+1]])
        return temp[1]
    
    new_size = (size // 2)
    temp = sorted([solve(new_size, r, c), solve(new_size, r, c + new_size), solve(new_size, r + new_size, c), solve(new_size, r + new_size, c + new_size)])

    return temp[1]

n = int(input())
nums = [list(map(int, input().split())) for _ in range(n)]

if n == 1: print(nums[0][0])
else: print(solve(n, 0, 0))