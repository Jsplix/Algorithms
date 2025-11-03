import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline
# [BOJ] 17410 수열과 쿼리 1.5 / 제곱근 분할법
def update(idx, value):
    selected = bucket[idx // size]
    
    prev = arr[idx]
    pos = bisect_left(selected, prev)
    selected.pop(pos)
    
    new_pos = bisect_left(selected, value)
    selected.insert(new_pos, value)
    arr[idx] = value

def query(left, right, value):
    ret = 0
    
    while left % size != 0 and left <= right:
        ret += 1 if arr[left] > value else 0
        left += 1
    
    while (right + 1) % size != 0 and left <= right:
        ret += 1 if arr[right] > value else 0
        right -= 1
    
    while left <= right:
        selected = bucket[left // size]
        ret += len(selected) - bisect_right(selected, value)
        left += size
    
    return ret

LIM = 10 ** 6 + 100
N = int(input())
arr = [0] + list(map(int, input().split()))

size = 1200
bucket = [[] for _ in range(size)]

for i in range(1, N + 1):
    bucket[i // size].append(arr[i])

for bkt in bucket:
    bkt.sort()

M = int(input())
result = []
for _ in range(M):
    qry = list(map(int, input().split()))
    
    if qry[0] == 1:
        update(qry[1], qry[2])
    else:
        result.append(str(query(qry[1], qry[2], qry[3])))

sys.stdout.write("\n".join(result))