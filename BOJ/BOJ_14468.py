import sys
input = sys.stdin.readline
# [BOJ] 14468 소가 길을 건너간 이유 2 / 구현, 문자열
cow = input().rstrip()
alphabet = [-1 for _ in range(26)]
check = [0 for _ in range(52)]

count = 0
for i in range(52):
    idx = ord(cow[i])-ord('A')
    if alphabet[idx] == -1:
        alphabet[idx] = i
        check[i] += 1
    else:
        check[i] = check[alphabet[idx]] + 1
        check[alphabet[idx]] += 1
        count += check[alphabet[idx]:i].count(1)

print(count)