import sys
input = sys.stdin.readline
# [BOJ] 26162 인공 원소 / 브루트 포스, 정수론
arr = []
for _ in range(int(input())):
    arr.append(int(input()))

num = [1 for _ in range(max(arr) + 1)]
num[1] = 0

if max(arr) >= 2:
    num[2] = 1

for i in range(2, len(num)): # Sieve of Eratosthenes
    if not num[i]:
        continue

    for j in range(i + i, max(arr) + 1, +i):
        if num[j]:
            num[j] = 0

def solve(n): # checking
    if n == 1:
        return False
    
    for i in range(2, n):
        if num[n - i] and num[i]:
            return True
    
    return False

for i in range(len(arr)):
    if solve(arr[i]):
        print("Yes")
    else:
        print("No")