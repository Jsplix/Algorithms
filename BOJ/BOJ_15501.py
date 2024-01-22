import sys
input = sys.stdin.readline
# [BOJ] 15501 부당한 퍼즐 / 애드 혹
n = int(input())
arr = list(map(int, input().split()))
check = list(map(int, input().split()))

idx = check.index(arr[0])
fwd = check[idx:] + check[:idx]
rev = check[idx+1:] + check[:idx+1]
rev.reverse()

if arr == fwd or arr == rev:
    print("good puzzle")
else:
    print("bad puzzle") 