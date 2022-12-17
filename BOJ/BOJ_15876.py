import sys
input = sys.stdin.readline
# [BOJ] 15876 Binary Counting / 수학
n, k = map(int, input().split())
bin_str = ''
x = 0

while len(bin_str) < n * 4 + k:
    bin_str += bin(x)[2:]
    x += 1

print(bin_str[k - 1], bin_str[k - 1 + n], bin_str[k - 1 + 2 * n], bin_str[k - 1 + 3 * n], bin_str[k - 1 + 4 * n])