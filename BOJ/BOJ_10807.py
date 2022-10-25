import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
s_num = int(input())

print(arr.count(s_num))