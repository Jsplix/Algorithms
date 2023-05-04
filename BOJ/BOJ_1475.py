import sys
input = sys.stdin.readline
# [BOJ] 1475 방 번호 / 구현
n = input().rstrip()
n_len = len(n)
num_set = {i: n_len for i in range(10)}

for x in n:
    x = int(x)
    if x == 6 or x == 9:
        if num_set[6] > num_set[9]: num_set[6] -= 1
        else: num_set[9] -= 1
    else:
        num_set[x] -= 1

num_set_value = list(num_set.values())
print(n_len - min(num_set_value))