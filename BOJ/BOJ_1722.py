import sys
input = sys.stdin.readline
# [BOJ] 1722 순열의 순서 / 수학, 구현, 조합론
def kth_permutations(n, k):
    k -= 1
    
    nums = [i for i in range(1, n + 1)]
    
    ret = []
    for i in range(n):
        x = k // f[n - i - 1]
        k %= f[n - i - 1]
        
        ret.append(nums.pop(x))
    
    return ret

n = int(input())
k, *arr = list(map(int, input().split()))

f = [1, 1, 2, 6]
for i in range(4, n + 1):
    f.append(f[i - 1] * i)
    
    
if k == 1:
    result = kth_permutations(n, arr[0])
    print(*result)
else:
    result = 1
    nums = [i for i in range(1, n + 1)]
    for i in range(n):
        x = nums.index(arr[i])
        result += x * f[n - i - 1]
        nums.remove(arr[i])
    print(result)