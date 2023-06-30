import sys
input = sys.stdin.readline
# [BOJ] 2161 카드 1 / 구현, 자료 구조, 큐
arr = [i for i in range(1, int(input())+1)]
li = []
while len(arr) != 1:
    li.append(arr.pop(0))
    arr.append(arr.pop(0))
print(*li, *arr)