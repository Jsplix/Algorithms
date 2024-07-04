import sys
from itertools import permutations
input = sys.stdin.readline
# [BOJ] 16945 매직 스퀘어로 변경하기 / 브루트 포스, 백트래킹
def isMagic(lst: list):
    if lst[0] + lst[4] + lst[8] != 15: return False
    if lst[2] + lst[4] + lst[6] != 15: return False

    if lst[0] + lst[1] + lst[2] != 15: return False
    if lst[3] + lst[4] + lst[5] != 15: return False
    if lst[6] + lst[7] + lst[8] != 15: return False

    if lst[0] + lst[3] + lst[6] != 15: return False
    if lst[1] + lst[4] + lst[7] != 15: return False
    if lst[2] + lst[5] + lst[8] != 15: return False

    return True

arr = []
for _ in range(3):
    arr += list(map(int, input().split()))

possible = list(permutations([i for i in range(1, 10)], 9))

result = 1001
for check in possible:
    if isMagic(check):
        temp = 0
        for i in range(9):
            temp += abs(check[i] - arr[i])
        
        result = min(temp, result)
print(result)