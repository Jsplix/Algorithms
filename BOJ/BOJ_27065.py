import sys
input = sys.stdin.readline
# [BOJ] 27065 2022년이 아름다웠던 이유 / 수학, 구현, 정수론, 소수 판정
def solve():
    # 과잉수 - True
    nums = [False for _ in range(5001)]
    
    for i in range(2, 5001):
        temp = 1
        for j in range(2, (i//2)+1):
            if i % j == 0: temp += j

        if i < temp: nums[i] = True

    return nums
    
result = solve()
for _ in range(int(input())):
    n = int(input())
    if result[n]:
        flag = False
        for i in range(1, (n//2)+1):
            if n % i == 0 and result[i]:
                flag = True
        
        if not flag: print("Good Bye")
        else: print("BOJ 2022")
    else: print("BOJ 2022")