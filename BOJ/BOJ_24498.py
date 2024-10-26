import sys
input = sys.stdin.readline
# [BOJ] 24498 blobnom / 그리디
n = int(input())
blobs = list(map(int, input().split()))

result = max(blobs)
for i in range(1, n-1):
    if min(blobs[i-1], blobs[i+1]) > 0:
        result = max(result, blobs[i] + min(blobs[i-1], blobs[i + 1]))
print(result)